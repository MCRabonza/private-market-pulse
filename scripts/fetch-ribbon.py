#!/usr/bin/env python3
"""
fetch-ribbon.py
KRV Private Market Pulse — Daily ribbon data fetcher.

Refreshes /home/user/workspace/krv-dark/data/ribbon-data.json with T-1 values
for FX, ASEAN-2 indices, US 10Y, DXY, and EM credit ETFs (CEMB + HYEM).

Schedule: weekday 07:00 Asia/Bangkok via schedule_cron `1716516a`.

Architecture (v1.1, post-cleanup 13 May 2026):
- All market data via Yahoo Finance public chart API (one pipe, retry-on-fail).
- FX:        USDTHB=X, USDPHP=X, USDIDR=X, USDVND=X
- Indices:   ^SET.BK (Thailand), ^JKSE (Indonesia)
- US 10Y:    ^TNX (CBOE 10-Year Treasury Yield Index — replaces FRED DGS10)
- DXY:       DX-Y.NYB
- EM credit: CEMB (iShares JPM EM Corp Bond), HYEM (VanEck EM HY Bond)
- Policy rates (BoT/BSP/BI/SBV): agent-maintained on MPC dates; this script
  preserves their values and only refreshes the dataset-level timestamps.

Dropped 13 May 2026 (fragile / unreliable feeds):
- PSEi          (Yahoo PSEI.PS unreliable)
- VN-Index      (Yahoo ^VNI returns null close field)
- EM Corp OAS   (FRED BAMLEMCBPIOAS — repeated timeouts; CEMB price proxy used instead)

Degraded-refresh policy: if < 10 of the 14 ribbon items refresh successfully,
the script writes nothing and exits 2. The cron will not commit. Caller
should send an in-app notification listing failed items.

Output: replaces ribbon-data.json in-place with last_refreshed_utc and
last_refreshed_label updated.
"""

from __future__ import annotations
import json
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "ribbon-data.json"
BANGKOK = timezone(timedelta(hours=7))

# ---- Symbol map ----------------------------------------------------------

YAHOO_SYMBOLS = {
    # FX — Yahoo USDxxx=X returns xxx per USD (correct orientation for our display)
    "thb":   "USDTHB=X",
    "php":   "USDPHP=X",
    "idr":   "USDIDR=X",
    "vnd":   "USDVND=X",
    # Indices
    "set":   "^SET.BK",
    "jci":   "^JKSE",
    # US 10Y as yield index (already in percent units)
    "us10y": "^TNX",
    # DXY
    "dxy":   "DX-Y.NYB",
    # EM credit proxies (replaces EM Corp OAS line)
    "cemb":  "CEMB",
    "hyem":  "HYEM",
}

# Policy rates are agent-maintained — script never overwrites them.
POLICY_RATE_IDS = {"bot", "bsp", "bi", "sbv"}

# ---- Fetchers ------------------------------------------------------------

def fetch_yahoo(symbol: str, retries: int = 3) -> tuple[float, float] | None:
    """Returns (last_close, pct_change_MoM) or None.

    Retries with exponential backoff. Skips null close values which cause
    the old ^VNI failure mode.
    """
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        f"?interval=1d&range=2mo"
    )
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "krv-pulse-ribbon/1.1"},
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
            result = data.get("chart", {}).get("result")
            if not result:
                last_err = "no chart result"
                time.sleep(2 ** attempt)
                continue
            quote = result[0].get("indicators", {}).get("quote", [{}])[0]
            closes_raw = quote.get("close", [])
            closes = [c for c in closes_raw if c is not None]
            if len(closes) < 22:
                last_err = f"only {len(closes)} valid closes (need 22 for MoM)"
                time.sleep(2 ** attempt)
                continue
            last = closes[-1]
            month_ago = closes[-22]
            pct = (last - month_ago) / month_ago * 100
            return last, pct
        except (urllib.error.URLError, KeyError, IndexError, TypeError, ValueError) as e:
            last_err = str(e)
            time.sleep(2 ** attempt)
    print(f"  Yahoo fetch failed for {symbol} after {retries} attempts: {last_err}",
          file=sys.stderr)
    return None


# ---- Formatters ----------------------------------------------------------

def fmt_value(item_id: str, raw: float) -> str:
    if item_id in ("thb", "php"):
        return f"{raw:.2f}"
    if item_id in ("idr", "vnd"):
        return f"{int(round(raw)):,}"
    if item_id in ("set", "jci"):
        return f"{raw:,.2f}"
    if item_id == "dxy":
        return f"{raw:.2f}"
    if item_id == "us10y":
        # ^TNX is yield × 1 (e.g. 4.31 means 4.31%); some feeds return ×10. Heuristic:
        v = raw / 10 if raw > 25 else raw
        return f"{v:.2f}%"
    if item_id in ("cemb", "hyem"):
        return f"{raw:.2f}"
    return f"{raw}"


# ---- Main ----------------------------------------------------------------

def main() -> int:
    data = json.loads(DATA_PATH.read_text())
    updated_ids: list[str] = []
    failed_ids: list[str] = []

    for item in data["items"]:
        iid = item["id"]
        if iid in POLICY_RATE_IDS:
            # Agent-maintained — preserve value and delta. Count as success.
            updated_ids.append(iid)
            continue
        if iid not in YAHOO_SYMBOLS:
            failed_ids.append(iid)
            continue

        result = fetch_yahoo(YAHOO_SYMBOLS[iid])
        if result is None:
            failed_ids.append(iid)
            continue

        last, pct = result
        item["value"] = fmt_value(iid, last)

        if iid == "us10y":
            # delta in bps not percent of pct
            v_now = last / 10 if last > 25 else last
            v_then = v_now / (1 + pct / 100) if pct != 0 else v_now
            item["delta_bps"] = int(round((v_now - v_then) * 100))
            item["delta_unit"] = "bps"
            item.pop("delta_pct", None)
        else:
            item["delta_pct"] = round(pct, 1)
            item["delta_unit"] = "MoM"
            item.pop("delta_bps", None)

        updated_ids.append(iid)

    total = len(data["items"])
    refreshed = len(updated_ids)

    if refreshed < 10:
        print(
            f"Ribbon refresh DEGRADED: only {refreshed}/{total} items "
            f"refreshed. Failed: {failed_ids}",
            file=sys.stderr,
        )
        return 2

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    now_bkk = now_utc.astimezone(BANGKOK)
    data["last_refreshed_utc"] = now_utc.isoformat().replace("+00:00", "Z")
    data["last_refreshed_label"] = now_bkk.strftime("%-d %b %Y · %H:%M ICT")

    DATA_PATH.write_text(json.dumps(data, indent=2) + "\n")
    print(
        f"Ribbon updated: {refreshed}/{total} items at "
        f"{data['last_refreshed_label']}. Failed: {failed_ids or 'none'}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
