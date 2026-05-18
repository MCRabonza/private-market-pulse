#!/usr/bin/env python3
"""
fetch-ribbon.py — KRV Private Market Pulse · ribbon data transform helper.

PIPELINE v2 (May 2026): Yahoo Finance + FRED are DEAD. The ribbon refresh is
now driven by the agent calling the Perplexity finance connector directly
(finance_quotes + finance_ohlcv_histories). This script no longer makes any
network calls — it is a pure transform that takes connector output and writes
ribbon-data.json in the correct schema.

Input (stdin, JSON):
{
  "quotes": {
    "USDTHB":   {"price": 32.78, "previousClose": 32.65},
    "USDPHP":   {...},
    "USDIDR":   {...},
    "USDVND":   {...},
    "^SET.BK":  {...},
    "^JKSE":    {...},
    "DX-Y.NYB": {...},
    "^TNX":     {...},
    "CEMB":     {...},
    "HYEM":     {...}
  },
  "histories": {
    "USDTHB": [{"date":"2026-04-15","close":32.05}, ..., {"date":"2026-05-15","close":32.78}],
    ...
  }
}

Output: writes /home/user/workspace/krv-dark/data/ribbon-data.json with MoM
deltas computed from histories (latest close vs first close ~30 days back).

Policy rates (BoT/BSP/BI/SBV) are preserved from the existing file — they are
agent-maintained on MPC dates and never touched by this transform.

Usage:
  cat connector-output.json | python3 fetch-ribbon.py
  python3 fetch-ribbon.py --input connector-output.json
"""

from __future__ import annotations
import json
import sys
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "ribbon-data.json"
BANGKOK = timezone(timedelta(hours=7))

# Ribbon layout: connector ticker → ribbon item id + label + formatter
LAYOUT = [
    ("USDTHB",   "thb",   "THB / USD",    "fx_2dp"),
    ("USDPHP",   "php",   "PHP / USD",    "fx_2dp"),
    ("USDIDR",   "idr",   "IDR / USD",    "int_comma"),
    ("USDVND",   "vnd",   "VND / USD",    "int_comma"),
    ("^SET.BK",  "set",   "SET",          "idx_2dp"),
    ("^JKSE",    "jci",   "JCI",          "idx_2dp"),
    # Policy rates inserted here from existing file (bot/bsp/bi/sbv)
    ("^TNX",     "us10y", "US 10Y",       "pct_bps"),
    ("DX-Y.NYB", "dxy",   "DXY",          "idx_2dp"),
    ("CEMB",     "cemb",  "EM IG CORP",   "etf_2dp"),
    ("HYEM",     "hyem",  "EM HY CORP",   "etf_2dp"),
]

POLICY_IDS = ["bot", "bsp", "bi", "sbv"]


def fmt_value(kind: str, v: float) -> str:
    if kind == "fx_2dp":     return f"{v:.2f}"
    if kind == "int_comma":  return f"{int(round(v)):,}"
    if kind == "idx_2dp":    return f"{v:,.2f}"
    if kind == "etf_2dp":    return f"{v:.2f}"
    if kind == "pct_bps":    return f"{v:.2f}%"
    return f"{v}"


def compute_mom(history: list):
    """Return MoM % change: latest close vs first close in window."""
    if not history or len(history) < 2:
        return None
    closes = [h["close"] for h in history if h.get("close") is not None]
    if len(closes) < 2:
        return None
    first, last = closes[0], closes[-1]
    if first == 0:
        return None
    return round((last - first) / first * 100, 1)


def compute_bps(history: list):
    """Return MoM bps change for yield series like ^TNX."""
    if not history or len(history) < 2:
        return None
    closes = [h["close"] for h in history if h.get("close") is not None]
    if len(closes) < 2:
        return None
    return int(round((closes[-1] - closes[0]) * 100))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="Path to connector JSON (else stdin)")
    args = ap.parse_args()

    if args.input:
        payload = json.loads(Path(args.input).read_text())
    else:
        payload = json.loads(sys.stdin.read())

    quotes = payload.get("quotes", {})
    histories = payload.get("histories", {})

    # Preserve existing policy rates (agent-maintained on MPC dates)
    existing = json.loads(DATA_PATH.read_text()) if DATA_PATH.exists() else {"items": []}
    policy = {it["id"]: it for it in existing.get("items", []) if it["id"] in POLICY_IDS}

    items = []
    # First block: FX + ASEAN indices
    for ticker, _id, label, fmt_kind in LAYOUT[:6]:
        q = quotes.get(ticker)
        if not q:
            print(f"[warn] missing quote: {ticker}", file=sys.stderr)
            continue
        price = q.get("price") or q.get("previousClose")
        mom = compute_mom(histories.get(ticker, []))
        items.append({
            "id": _id,
            "label": label,
            "value": fmt_value(fmt_kind, price),
            "delta_pct": mom if mom is not None else 0.0,
            "delta_unit": "MoM",
        })

    # Policy rates block (preserved verbatim)
    for pid in POLICY_IDS:
        if pid in policy:
            items.append(policy[pid])

    # Second block: yields, DXY, EM credit
    for ticker, _id, label, fmt_kind in LAYOUT[6:]:
        q = quotes.get(ticker)
        if not q:
            print(f"[warn] missing quote: {ticker}", file=sys.stderr)
            continue
        price = q.get("price") or q.get("previousClose")
        if _id == "us10y":
            bps = compute_bps(histories.get(ticker, []))
            items.append({
                "id": _id,
                "label": label,
                "value": fmt_value(fmt_kind, price),
                "delta_bps": bps if bps is not None else 0,
                "delta_unit": "bps",
            })
        else:
            mom = compute_mom(histories.get(ticker, []))
            items.append({
                "id": _id,
                "label": label,
                "value": fmt_value(fmt_kind, price),
                "delta_pct": mom if mom is not None else 0.0,
                "delta_unit": "MoM",
            })

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    now_bkk = now_utc.astimezone(BANGKOK)
    out = {
        "schema_version": "2.0",
        "last_refreshed_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "last_refreshed_label": now_bkk.strftime("%-d %b %Y · %H:%M ICT"),
        "pipeline": "perplexity-finance-connector",
        "items": items,
        "sources": {
            "fx": "Perplexity finance connector (USDTHB, USDPHP, USDIDR, USDVND)",
            "indices": "Perplexity finance connector (^SET.BK, ^JKSE)",
            "policy_rates": "BoT MPC / BSP MB / BI / SBV official releases — agent-maintained on MPC dates",
            "us10y": "Perplexity finance connector (^TNX)",
            "dxy": "Perplexity finance connector (DX-Y.NYB)",
            "em_credit": "Perplexity finance connector (CEMB iShares J.P. Morgan EM Corp Bond ETF; HYEM VanEck EM High Yield Bond ETF)",
        },
    }

    DATA_PATH.write_text(json.dumps(out, indent=2) + "\n")
    refreshed = sum(1 for it in items if it["id"] not in POLICY_IDS)
    total_live = len(LAYOUT)  # 10 live items expected
    print(f"[ok] wrote {DATA_PATH} · {refreshed}/{total_live} live items refreshed", file=sys.stderr)
    return 0 if refreshed >= 8 else 2


if __name__ == "__main__":
    sys.exit(main())
