#!/usr/bin/env python3
"""
fetch-ribbon.py
KRV Private Market Pulse — Daily ribbon data fetcher.

Refreshes /home/user/workspace/krv-dark/data/ribbon-data.json with T-1 values
for FX, ASEAN-4 indices, policy rates, US 10Y, DXY, and EM Corp OAS.

Schedule: weekday 07:00 Asia/Bangkok via schedule_cron.

Sources (primary → fallback):
- FX: exchangerate.host (free) → Yahoo Finance
- Indices: Yahoo Finance (^SET.BK, PSEI.PS, ^JKSE, ^VNI)
- US 10Y: FRED DGS10
- DXY: Yahoo Finance DX-Y.NYB
- EM Corp OAS: FRED BAMLEMCBPIOAS
- Policy rates: maintained manually (change on MPC dates; script only updates
  the delta vs prior month, not the value itself)

Output: replaces ribbon-data.json in-place with last_refreshed_utc and
last_refreshed_label updated to UTC now + Bangkok local time.
"""

from __future__ import annotations
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "ribbon-data.json"
BANGKOK = timezone(timedelta(hours=7))

# ---- Symbol map ----------------------------------------------------------

YAHOO_SYMBOLS = {
    "thb":     "THBUSD=X",   # then invert
    "php":     "PHPUSD=X",
    "idr":     "IDRUSD=X",
    "vnd":     "VNDUSD=X",
    "set":     "^SET.BK",
    "psei":    "PSEI.PS",
    "jci":     "^JKSE",
    "vnindex": "^VNI",
    "dxy":     "DX-Y.NYB",
}

FRED_SERIES = {
    "us10y":  "DGS10",
    "emcorp": "BAMLEMCBPIOAS",
}

# Policy rates are agent-maintained (updated on MPC dates manually)
# This script only refreshes timestamps for policy-rate rows.

# ---- Fetchers ------------------------------------------------------------

def fetch_yahoo(symbol: str) -> tuple[float, float] | None:
    """Returns (last_price, pct_change_1m) or None."""
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        f"?interval=1d&range=2mo"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "krv-pulse-ribbon/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        result = data["chart"]["result"][0]
        closes = [c for c in result["indicators"]["quote"][0]["close"] if c is not None]
        if len(closes) < 22:
            return None
        last = closes[-1]
        month_ago = closes[-22]
        pct = (last - month_ago) / month_ago * 100
        return last, pct
    except (urllib.error.URLError, KeyError, IndexError, TypeError) as e:
        print(f"  Yahoo fetch failed for {symbol}: {e}", file=sys.stderr)
        return None


def fetch_fred(series: str) -> tuple[float, float] | None:
    """FRED public CSV — no API key needed for daily series."""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "krv-pulse-ribbon/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            lines = resp.read().decode().strip().split("\n")
        rows = []
        for line in lines[1:]:
            parts = line.split(",")
            if len(parts) < 2 or parts[1] in (".", ""):
                continue
            try:
                rows.append(float(parts[1]))
            except ValueError:
                continue
        if len(rows) < 22:
            return None
        return rows[-1], rows[-1] - rows[-22]
    except (urllib.error.URLError, ValueError) as e:
        print(f"  FRED fetch failed for {series}: {e}", file=sys.stderr)
        return None


# ---- Formatters ----------------------------------------------------------

def fmt_value(item_id: str, raw: float) -> str:
    if item_id in ("thb", "php"):
        return f"{1/raw:.2f}" if raw < 1 else f"{raw:.2f}"
    if item_id in ("idr", "vnd"):
        return f"{int(1/raw):,}" if raw < 1 else f"{int(raw):,}"
    if item_id in ("set", "psei", "jci", "vnindex"):
        return f"{raw:,.2f}"
    if item_id == "dxy":
        return f"{raw:.2f}"
    if item_id == "us10y":
        return f"{raw:.2f}%"
    if item_id == "emcorp":
        return f"{int(round(raw))} bps"
    return f"{raw}"


# ---- Main ----------------------------------------------------------------

def main() -> int:
    data = json.loads(DATA_PATH.read_text())
    updated = 0

    for item in data["items"]:
        iid = item["id"]
        if iid in YAHOO_SYMBOLS:
            result = fetch_yahoo(YAHOO_SYMBOLS[iid])
            if result is not None:
                last, pct = result
                item["value"] = fmt_value(iid, last)
                item["delta_pct"] = round(pct, 1)
                updated += 1
        elif iid in FRED_SERIES:
            result = fetch_fred(FRED_SERIES[iid])
            if result is not None:
                last, delta = result
                item["value"] = fmt_value(iid, last)
                if iid == "us10y":
                    item["delta_bps"] = int(round(delta * 100))
                else:
                    item["delta_bps"] = int(round(delta))
                updated += 1

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    now_bkk = now_utc.astimezone(BANGKOK)
    data["last_refreshed_utc"] = now_utc.isoformat().replace("+00:00", "Z")
    data["last_refreshed_label"] = now_bkk.strftime("%-d %b %Y · %H:%M ICT")

    DATA_PATH.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Ribbon updated: {updated}/{len(data['items'])} live items at {data['last_refreshed_label']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
