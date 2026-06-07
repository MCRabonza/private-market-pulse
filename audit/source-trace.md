# Source Trace — pulse.krv.co

**Status:** v0.1 · skeleton committed to make the source-trace gap visible on `main`
**Owner:** agent (compilation) · MCR (approval)
**Last updated:** 2026-06-07
**Filed against:** ISSUE-001 — reproducibility files missing from `main`

---

## 0. Rule

Every number rendered on pulse.krv.co must appear in this file with: (a) the section that uses it, (b) the primary URL, (c) the retrieval date. The Master Index is never cited — only underlying primary sources.

Until a number's row here is filled, the number is flagged as **pre-trace, audit-pending** but not removed from the dashboard. The list of pre-trace numbers below is the work queue to close.

---

## 1. Section 01 — K-Opp Index

| Number | Value | Section | Primary source | Retrieval date | Status |
|---|---|---|---|---|---|
| K-Opp Index headline | 395 bps (Jan 2026) | Section 01 hero | Derived: mean of Panel 03 country premia per `audit/k-opp-methodology.md` §7 — reconciles to (540+476+335+230)/4 = 395.25 → 395 | 2026-06-07 | **Verified** |
| Thailand SME premium | 476 bps | Section 01 Panel 03 | BoT FM_RT_001_S3 by contract size — SME ≤ THB 100M (8.91%), Corporate ≥ THB 500M (4.15%). [app.bot.or.th](https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=1011&language=ENG) | 2026-06-07 | **Verified** (per k-opp-methodology.md §3) |
| Philippines SME premium | 540 bps | Section 01 Panel 03 | BSP Weekly Lending Rates by Type of Loan — SME effective rate, week ending 31 Dec 2025, high 11.30% − low 5.90%. [bsp.gov.ph](https://www.bsp.gov.ph/Statistics/Financial%20System%20Accounts/weeklylendingratestype.aspx) · Quarterly cross-check: [LTP_3qtr2025.pdf](https://www.bsp.gov.ph/Lists/Quarterly%20Report/Attachments/27/LTP_3qtr2025.pdf) | 2026-06-07 | **Verified** (per k-opp-methodology.md §4) |
| Indonesia SME premium | 335 bps | Section 01 Panel 03 | BI SEKI Table I.26 working capital rate 8.06% + OJK June 2025 MSME-over-corporate premium ≈ 335 bps, layered. [bi.go.id SEKI I.26](https://www.bi.go.id/seki/tabel/TABEL1_26.pdf) · [OJK premium via Databoks](https://databoks.katadata.co.id/en/finance/statistics/68d6250452dcf/msme-loan-interest-rates-in-indonesia-higher-than-corporate-loans-june-2025) | 2026-06-07 | **Verified** (per k-opp-methodology.md §5; OJK premium carries forward between publications) |
| Vietnam SME premium | 230 bps | Section 01 Panel 03 | VNBA / SBV monthly VND lending rate range, top 9.70% − bottom 7.40%; priority-sector capped lending excluded. [vnba.org.vn](https://vnba.org.vn/en/interest-rate-developments-applied-by-credit-institutions-in-march-2026-21553.htm) | 2026-06-07 | **Verified** (per k-opp-methodology.md §6; understated by priority-cap exclusion — declared limitation) |
| K-Opp 19-month series | array in `data/k-opp-series.json` | Section 01 Panel 02 | Back-tested under v1.0 method per k-opp-methodology.md §13 | 2026-06-07 | Back-test labelled; per-month primary-source re-fetch is next audit work-item |
| EM Corp OAS series | array | Section 01 Panel 02 | ICE BofA Emerging Markets Corporate Plus Index OAS — [FRED BAMLEMCBPIOAS](https://fred.stlouisfed.org/series/BAMLEMCBPIOAS) | 2026-06-07 | **Verified** (benchmark series, not K-Opp input) |
| Asia EM Corp OAS series | array | Section 01 Panel 02 | ICE BofA Asia EM Corporate Plus Index OAS — [FRED BAMLEMRACRPIASIAOAS](https://fred.stlouisfed.org/series/BAMLEMRACRPIASIAOAS) | 2026-06-07 | **Verified** (benchmark) |
| US HY OAS series | array | Section 01 Panel 02 | ICE BofA US High Yield Index OAS — [FRED BAMLH0A0HYM2](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) | 2026-06-07 | **Verified** (benchmark) |
| US IG OAS series | array | Section 01 Panel 02 | ICE BofA US Corporate Master OAS — [FRED BAMLC0A0CM](https://fred.stlouisfed.org/series/BAMLC0A0CM) | 2026-06-07 | **Verified** (benchmark; combines with HY for Net Opacity Premium per methodology §8) |
| Net Opacity Premium | 197 bps (Jan 2026) | Section 01 (derived) | Derived: K-Opp − (US HY OAS − US IG OAS) per k-opp-methodology.md §8 | 2026-06-07 | **Verified** (derived) |
| IFC 2005 Frontier Markets anchor | 400 bps (fixed) | Section 01 reference line | Practitioner anchor, M.C.R. IFC 2005 vintage; not a published index | static | **Declared** as practitioner anchor (limitation §12.3) |

---

## 2. Section 02 — The Defining Problem (SME Funding Gap)

| Number | Value | Primary source | Retrieval date | Status |
|---|---|---|---|---|
| Global MSME finance gap | USD 5.7T | IFC / SME Finance Forum — MSME Finance Gap https://www.smefinanceforum.org/data-sites/msme-finance-gap | _pending recovery_ | Audit pending |
| Asia-Pacific share | 46% / USD 2.6T | IFC MSME Finance Gap | _pending recovery_ | Audit pending |
| ASEAN-4 aggregate | USD 450B+ | Composite: IFC + ADB Asia SME Monitor + national SME agencies | _pending recovery_ | Audit pending |
| Indonesia gap range | USD 165–234B | _MCR-INPUT-REQUIRED_ (was flagged in canon for re-fetch) | _pending_ | Re-fetch flagged in `krv-private-market-pulse` §9 |
| Philippines gap | USD 210B | _MCR-INPUT-REQUIRED_ (re-fetch flagged) | _pending_ | Re-fetch flagged |
| Thailand aggregate gap | ~USD 50B | _MCR-INPUT-REQUIRED_ (re-fetch flagged) | _pending_ | Re-fetch flagged |
| Vietnam gap | USD 21.7B | _MCR-INPUT-REQUIRED_ | _pending_ | Audit pending |

---

## 3. Section 03 — Country Focus: Thailand

| Number | Value | Primary source | Retrieval date | Status |
|---|---|---|---|---|
| Number of SMEs | 3.2M | OSMEP annual report — https://www.sme.go.th/ | _pending recovery_ | Audit pending |
| Number of CPAs | 74,000 | TFAC (Federation of Accounting Professions) annual report — https://www.tfac.or.th/ | _pending recovery_ | Audit pending |
| SME loans YoY Q4 2025 | −4.1% | BoT Financial Stability Report — https://www.bot.or.th/en/research-and-publications/articles-and-publications/financial-stability-report.html | _pending recovery_ | Audit pending |
| NPL ratio (SME) Q3 2025 | 7.2% | BoT FSR | _pending recovery_ | Audit pending |
| Stage 2 ratio | 11.7% | BoT FSR | _pending recovery_ | Audit pending |
| BoT policy rate (Feb 2026) | 1.00% | BoT MPC release — https://www.bot.or.th/en/our-roles/monetary-policy/mpc-publication.html | _pending recovery_ | Audit pending |

---

## 4. Section 04 — The Rate Paradox

| Number | Value | Primary source | Retrieval date | Status |
|---|---|---|---|---|
| BoT rate path | 1.75% → 1.00% | BoT MPC archive | _pending_ | Audit pending |
| NPL trend | 3.8% → 7.2% | BoT FSR | _pending_ | Audit pending |
| SME vs Corporate risk weight | 85–100% vs 20% | [BCBS Basel III](https://www.bis.org/bcbs/basel3.htm) + [BoT capital adequacy framework](https://www.bot.or.th/en/financial-institutions/key-regulations/capital-adequacy.html); also documented in `audit/cost-stack-methodology.md` §2 Layer D | 2026-06-07 | **Verified** — static reg, low refresh need |
| Cost stack | 9.5–13.5% | Derived: four-layer bottom-up build per `audit/cost-stack-methodology.md` v1.0 §2. Underlying provisioning layer cites [BoT Financial Stability Review Q3 2025](https://www.bot.or.th/en/research-and-publications/articles-and-publications/financial-stability-report.html) (System Stage 2 7.2%, SME Stage 3 NPL 9.35%, Stage 2 11.7% of book) | 2026-06-07 | **Verified** (closes ISSUE-002) |
| SME loan portfolio yield | 8–10% | BoT lending rate statistics blended with non-bank SME yields per IFC ASEAN SME Finance reports; documented in `audit/cost-stack-methodology.md` §4 | 2026-06-07 | **Verified** |
| Negative spread | −1% to −5% | Derived: yield (8–10%) minus cost stack (9.5–13.5%) per `audit/cost-stack-methodology.md` §4 | 2026-06-07 | **Verified** (derived) |

---

## 5. Section 05 — Regional Pattern

| Number | Value | Primary source | Retrieval date | Status |
|---|---|---|---|---|
| Indonesia MSME loan growth Feb 2026 | −0.06% YoY | BI Statistik Ekonomi Keuangan Indonesia (SEKI) — https://www.bi.go.id/en/statistik/ | _pending recovery_ | Audit pending |
| Indonesia total banking credit growth | +9.37% | BI SEKI | _pending recovery_ | Audit pending |
| Indonesia MSME count | 66M | Kementerian Koperasi & UKM annual report — https://www.kemenkopukm.go.id/ | _pending_ | Audit pending |
| Indonesia MSME share of GDP | 61% | Kementerian Koperasi annual | _pending_ | Audit pending |
| Philippines MSME credit share | 4.6% | BSP financial stability / SLS — https://www.bsp.gov.ph/SitePages/MediaAndResearch/FinancialStability.aspx | _pending_ | Audit pending |
| Philippines Magna Carta mandate | 10% | Republic Act 6977 as amended by RA 9501 | static | Static law |
| Vietnam EuroCham BCI | 83.0 | EuroCham Vietnam quarterly publication — https://eurochamvn.org/business-confidence-index/ | _pending_ | **FLAGGED in canon — re-verify each quarter** |
| ASEAN unmet SME credit need | 60–65% | ADB Asia SME Monitor — https://www.adb.org/publications/series/asia-sme-monitor | _pending recovery_ | Audit pending |

---

## 6. Sections 06–07 — Accountancy Gap

| Number | Value | Primary source | Retrieval date | Status |
|---|---|---|---|---|
| Thailand CPA-to-SME ratio | 0.9 per 1,000 SMEs | Derived: TFAC CPA count / OSMEP SME count | computed from §3 inputs | Audit pending |
| Philippines CPA-to-SME ratio | 1.7 per 1,000 SMEs | Derived: PRC-BoA CPA count / DTI SME count | _pending recovery_ | Audit pending |
| Indonesia CPA-to-SME ratio | 0.3 per 1,000 SMEs | Derived: IAPI (Institut Akuntan Publik Indonesia) / Kementerian Koperasi | _pending recovery_ | Audit pending |
| Vietnam CPA-to-SME ratio | 1.2 per 1,000 SMEs | Derived: VAA (Vietnam Association of Accountants and Auditors) / SBV SME count | _pending recovery_ | Audit pending |
| OECD benchmark | 8–12 per 1,000 SMEs | OECD SME and Entrepreneurship Outlook — https://www.oecd.org/en/publications/oecd-sme-and-entrepreneurship-outlook_25166679.html | _pending_ | Audit pending |
| Thailand <5% of SMEs audited annually | <5% | TFAC + Department of Business Development | _pending_ | Audit pending |
| Thailand >60% of CPAs retire this decade | >60% | TFAC member demographics | _pending_ | Audit pending |

---

## 7. Daily ribbon

The ribbon is owned by `ribbon-daily` cron (Perplexity finance connector). Live items refresh daily; their source is the connector itself (which aggregates from Yahoo/exchange feeds). Policy rates are agent-maintained per `mpc-watch` discipline. The connector-sourced items do not require per-row entries here, but the four policy rates do:

| Number | Value | Primary source | Retrieval date | Status |
|---|---|---|---|---|
| BoT policy rate | 1.00% | BoT MPC release — https://www.bot.or.th/en/our-roles/monetary-policy/mpc-publication.html | _pending — last update tracked in `data/ribbon-data.json`_ | Audit pending |
| BSP target RRP | 4.25% | BSP Monetary Policy Decisions — https://www.bsp.gov.ph/SitePages/MediaAndResearch/MonetaryPolicyDecisions.aspx | _pending_ | Audit pending |
| BI 7-Day Reverse Repo | 4.75% | BI news release — https://www.bi.go.id/en/publikasi/ruang-media/news-release/Default.aspx | _pending_ | Audit pending |
| SBV refinancing rate | 4.50% | SBV news — https://sbv.gov.vn/webcenter/portal/en/home/sbv/news/news_chitiet | _pending_ | Audit pending |

---

## 8. Audit close-out checklist

To close ISSUE-001's source-trace requirement, every row above with `_pending_` or `_MCR-INPUT-REQUIRED_` must resolve to: (a) primary URL, (b) ISO retrieval date, (c) status = `verified`.

Work queue:
- [ ] §1 K-Opp country premia: 4 rows pending MCR methodology input
- [ ] §1 K-Opp companion series: 4 rows pending FRED retrieval-date recovery
- [ ] §2 Defining Problem: 7 rows pending recovery
- [ ] §3 Thailand: 6 rows pending recovery
- [ ] §4 Rate Paradox: 5 rows pending recovery (1 KRV-internal needs methodology link)
- [ ] §5 Regional Pattern: 8 rows pending recovery
- [ ] §6 Accountancy Gap: 7 rows pending recovery
- [ ] §7 Daily ribbon policy rates: 4 rows pending recovery

**Estimate:** 41 rows to close. Agent can attempt re-fetch on rows where the primary URL is known (the majority); MCR input required only for the K-Opp methodology in §1 and the KRV cost-stack methodology link in §4.

When `source-audit-weekly` cron runs, it will crawl every URL above and report dead links per `pulse-living-maintenance/references/source-audit-runbook.md`.
