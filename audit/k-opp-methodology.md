# K-Opp Index — Methodology

**Status:** v1.0 · committed to `main`
**Owner:** MCR (method) · agent (computation, rendering, audit trail)
**Last updated:** 2026-06-07
**Companion editorial:** `Credit-Notes-No01-The-Opacity-Premium-DRAFT.md` (Space file). The Credit Note is the editorial reading of this method; this file is the canonical machine-readable recipe. **If the two ever drift, this file is authoritative.**

---

## 0. Statement of intent

The K-Opp Index is a published measurement. Its authority is computational, not editorial. The method below defines the index. The number is whatever the method produces from honest, primary-sourced inputs. The number is not set by preference.

Resolution paths when the monthly refresh produces an unexpected value:
(a) the inputs are wrong — re-fetch and recompute,
(b) the method is wrong — propose v1.1, write the rationale (§14), version the change, recompute the historical series under the new method,
(c) the answer is the news — publish a Credit Note explaining the regime shift.

Never: (d) overwrite the headline with a preferred number.

---

## 1. Canonical definition

**K-Opp Index** = the **ASEAN-4 SME-vs-corporate raw lending spread**, simple arithmetic mean across {Thailand, Philippines, Indonesia, Vietnam}, expressed in basis points.

For country *c* in month *t*:

```
s_raw[c,t] = ( r_SME[c,t] − r_CORP[c,t] )   expressed in bps
```

Where `r_SME[c,t]` is the country-specific **small-borrower lending-rate proxy** (§3–§6) and `r_CORP[c,t]` is the country-specific **large-corporate lending-rate proxy** (§3–§6). Each proxy is the cleanest publicly available reading; proxies are heterogeneous across the four countries by necessity (each central bank publishes a different breakout) and are named per-country in §3–§6.

The K-Opp Index is then:

```
K-Opp[t] = round_half_up( mean( s_raw[TH,t], s_raw[PH,t], s_raw[ID,t], s_raw[VN,t] ) )
```

**Current values (January 2026, the live publication):**

| Country | SME proxy rate | Corporate proxy rate | Raw spread | Source proxy | Cadence |
|---|---:|---:|---:|---|---|
| Thailand | 8.91% | 4.15% | **476 bps** | BoT FM_RT_001_S3 by contract size | Monthly |
| Philippines | 11.30% | 5.90% | **540 bps** | BSP Weekly Lending Rates — SME effective, high–low | Weekly |
| Indonesia | 11.41% | 8.06% | **335 bps** | BI SEKI I.26 working capital + OJK premium layer | Monthly |
| Vietnam | 9.70% | 7.40% | **230 bps** | VNBA range, top–bottom | Monthly |
| **ASEAN-4 simple mean (K-Opp)** | — | — | **395 bps** | (540+476+335+230)/4 = 395.25 → 395 | Monthly |

The headline reconciles to the four bars to the digit.

---

## 2. Cadence and anchoring

- **Refresh cadence:** monthly, published the **first Monday after the last of the four central-bank monthly bulletins prints** for the relevant month.
- **Anchor:** the most recently completed calendar month for which all four country proxies have been published.
- **Lag handling:** where a country lags on a quarterly cycle (Philippines BSP LTP runs quarterly), the higher-frequency print (BSP Weekly Lending Rates) is used for the monthly refresh and the quarterly LTP cross-checks at quarter-end. Lags are flagged in the audit log (§13).
- **Carry-forward:** if a country's source data is not published by month-end + 5 business days, the prior month's value carries forward with an explicit annotation. Carry-forward beyond 60 days requires MCR review.

---

## 3. Thailand SME premium — construction

**Current bar: 476 bps (January 2026).**

| Field | Value |
|---|---|
| Active source table | **BoT FM_RT_001_S3** — *Interest Rates in Financial Market — New Loan Rates for Businesses, by Contract Amount* |
| Source URL | https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=1011&language=ENG |
| SME proxy | New-loan rate for contract size **≤ THB 100M** (≈ USD 2.7M) |
| Corporate proxy | New-loan rate for contract size **≥ THB 500M** (≈ USD 13.5M) |
| Frequency | Monthly |
| Computation | `r_SME − r_CORP`, expressed in bps |
| January 2026 inputs | SME 8.91% · Corporate 4.15% |
| January 2026 spread | **476 bps** |
| Rounding | Half-up to the nearest integer bp |
| Known anti-pattern | **Do NOT use BoT FM_RT_001_S2** (legacy table). Its methodology does not map cleanly to the SME contract-size cut and collapses Thailand to ~60 bps. Earlier drafts of this method used S2 and were superseded. |

---

## 4. Philippines SME premium — construction

**Current bar: 540 bps (January 2026).**

| Field | Value |
|---|---|
| Active source | **BSP — Weekly Lending Rates by Type of Loan**, *SME Effective Rate* line |
| Source URL | https://www.bsp.gov.ph/Statistics/Financial%20System%20Accounts/weeklylendingratestype.aspx |
| Reading | Week ending **31 December 2025** (latest available at January 2026 print) |
| SME proxy | **High** of the published SME effective rate range |
| Corporate proxy | **Low** of the published range (cleanest available proxy for large-corporate end of the SME-eligible book) |
| Quarterly cross-check | BSP — *Loans to Productive Sectors Q3 2025*, https://www.bsp.gov.ph/Lists/Quarterly%20Report/Attachments/27/LTP_3qtr2025.pdf |
| Frequency | Weekly (monthly K-Opp uses last weekly print of the month) |
| January 2026 inputs | SME 11.30% · Corporate 5.90% |
| January 2026 spread | **540 bps** |
| Limitation declared | BSP does not publish a directly comparable "large corporate" rate. The high–low convention is the cleanest proxy available; alternates considered (PSE-listed corporate-bond yields) are not loan rates and are rejected. |

---

## 5. Indonesia SME premium — construction

**Current bar: 335 bps (January 2026).**

| Field | Value |
|---|---|
| Primary source — corporate base | **BI Statistik Ekonomi Keuangan Indonesia (SEKI), Table I.26** — *Commercial Banks Working Capital Rate* |
| Source URL | https://www.bi.go.id/seki/tabel/TABEL1_26.pdf |
| Layered source — MSME premium | **OJK** acknowledgment of MSME premium over corporate rates (June 2025 print) via Databoks Katadata, 26 September 2025 |
| Layered source URL | https://databoks.katadata.co.id/en/finance/statistics/68d6250452dcf/msme-loan-interest-rates-in-indonesia-higher-than-corporate-loans-june-2025 |
| Assembly formula | `r_SME[ID,t] = r_CORP[ID,t] + OJK_premium`, where `r_CORP` is the SEKI I.26 working-capital rate and `OJK_premium` is the OJK-published MSME-over-corporate premium (currently ~335 bps at the June 2025 reading; carried forward until the next OJK publication of MSME-rate detail) |
| Frequency | Monthly (SEKI I.26 publishes monthly; OJK premium publishes less frequently and is carried forward between publications) |
| January 2026 inputs | Corporate (SEKI I.26) 8.06% · OJK premium ≈ 335 bps · Implied SME 11.41% |
| January 2026 spread | **335 bps** (equals the OJK premium by construction; the SEKI base sets both legs) |
| Limitation declared | This is a **two-component layered proxy**, not a single-source spread. BI does not publish a working-capital rate split for MSMEs in SEKI I.26; the OJK premium is the cleanest acknowledgment of the gap. When BI begins publishing an MSME working-capital line directly, this method will be reissued as v1.1. |

---

## 6. Vietnam SME premium — construction

**Current bar: 230 bps (January 2026).**

| Field | Value |
|---|---|
| Primary source | **Vietnam Banks Association (VNBA) / State Bank of Vietnam (SBV)** — *Interest Rate Developments Applied by Credit Institutions* monthly report |
| Source URL | https://vnba.org.vn/en/interest-rate-developments-applied-by-credit-institutions-in-march-2026-21553.htm (latest available; January 2026 reading taken from the corresponding monthly publication) |
| SME proxy | **Top** of the published VND standard lending-rate range (excludes priority-sector capped lending) |
| Corporate proxy | **Bottom** of the same standard range |
| Priority-cap treatment | SBV caps **priority-sector** lending at 4%. This cap is **excluded** from both legs of the K-Opp computation. The priority-sector band is a regulatory floor, not a market-clearing rate; including it would mechanically suppress the published premium. |
| Frequency | Monthly |
| January 2026 inputs | Top 9.70% · Bottom 7.40% |
| January 2026 spread | **230 bps** |
| Limitation declared | **The true Vietnam SME premium is understated** by this proxy. The most opaque Vietnamese SMEs do not receive credit at all (priority caps make them uneconomic to lend to at any rate inside the cap; outside the cap, they are below the underwriting threshold). The 230 bps figure represents the priced premium on lent SMEs, not the implied premium on unlent ones. A "Vietnam — uncapped" alternate is planned for Q3 2026, using policy bank disclosures + private-credit fund quotes. |

---

## 7. Aggregation rule

```
K-Opp[t] = round_half_up( ( s_raw[TH,t] + s_raw[PH,t] + s_raw[ID,t] + s_raw[VN,t] ) / 4 )
```

- **Simple arithmetic mean.** Each ASEAN-4 economy counts as one observation. No GDP weighting, no banking-sector-size weighting, no SME-population weighting. The simple mean is the right aggregation because each country represents one observation of the same regional accountancy/credit-gap regime — not a fraction of an economic mass.
- **Rounding.** Half-up to the nearest integer basis point at the headline. Per-country bars are also reported as integers.
- **Reconciliation.** The published `headline_bps` in `data/k-opp-series.json` must equal this computation to the digit. The `renderKopp()` JavaScript on the dashboard enforces this — if the headline does not match the mean of the four bars, the renderer logs a console warning and refuses to update the headline element.

---

## 8. Companion series (Panel 02 — the legible benchmarks)

The K-Opp panel renders four benchmark series alongside the ASEAN-4 line. These are **not inputs to the K-Opp number** — they are the contrast against which the K-Opp is read in the Credit Note.

| Series | Source | FRED ticker | Role |
|---|---|---|---|
| EM Corporate OAS | ICE BofA Emerging Markets Corporate Plus Index OAS | `BAMLEMCBPIOAS` | Large-issuer EM credit spread in a legible market |
| Asia EM Corporate OAS | ICE BofA Asia EM Corporate Plus Index OAS | `BAMLEMRACRPIASIAOAS` | Regional cross-check, large issuers only |
| US HY OAS | ICE BofA US High Yield Index OAS | `BAMLH0A0HYM2` | Default/recovery risk in a fully legible market |
| US IG OAS | ICE BofA US Corporate Master OAS | `BAMLC0A0CM` | Used to compute US HY-IG spread for the Net Opacity Premium |
| IFC 2005 anchor | Practitioner reference, M.C.R. IFC 2005 vintage | — | Fixed at 400 bps as a historical parallel, not a moving comparable |

The **Net Opacity Premium** is a derived metric, also defined here:

```
NetOPP[t] = K-Opp[t] − ( US_HY_OAS[t] − US_IG_OAS[t] )
```

This is the spread the ASEAN SME pays *above* what default and recovery risk in a fully legible market would justify. As of January 2026: 395 − 198 = **197 bps**.

---

## 9. Guards (the index cannot be set by preference)

### 9.1 Reproducibility guard
A refresh is accepted only if `round_half_up((s_TH + s_PH + s_ID + s_VN) / 4) == headline_bps` to the digit. If the four bars and the headline do not reconcile, **neither is written** and the refresh halts with an MCR notification.

### 9.2 Discontinuity guard
If `|K-Opp[t] − K-Opp[t−1]| > 50 bps`, the refresh halts and emails MCR with the per-country breakdown. A >50 bp move is either a genuine regime shift (worth a Credit Note, not a silent refresh) or an input error. Either way, human review before commit.

### 9.3 Sign and range guard
Each `s_raw[c,t]` must be in `[0, 2000]` bps. Negative implies SMEs borrow cheaper than corporates (implausible under ASEAN regulatory regime); >2000 bps implies a national crisis worth its own Credit Note. Either triggers a halt.

### 9.4 No-override rule
The K-Opp number cannot be set by hand. The renderer reads `data/k-opp-series.json`; the JSON is written only by the monthly refresh procedure (§10). An override changes the method (versioned, §11), not the number.

### 9.5 Source-table guard (Thailand-specific)
The refresh procedure must verify it is reading **FM_RT_001_S3** and not FM_RT_001_S2. Reading S2 silently produces a wrong Thailand bar (~60 bps instead of ~476 bps). The fetch step must assert the table identifier in the response and halt if it sees S2.

---

## 10. Refresh procedure (monthly)

1. **Fetch** each country's primary source per §3–§6. Record retrieval timestamp and full URL in the audit log (§13).
2. **Per-country computation.** Compute `s_raw[c,t]` for each country using the country-specific formula. Apply Indonesia OJK-premium layering (§5) and Vietnam priority-cap exclusion (§6).
3. **Aggregation.** Compute `K-Opp[t]` per §7.
4. **Guards.** Run §9.1 reproducibility, §9.2 discontinuity, §9.3 sign/range, §9.5 source-table. Any halt blocks commit and notifies MCR.
5. **Write.** Append to `data/k-opp-series.json`: extend `months[]`, extend the K-Opp index series, update `headline_bps` and `headline_label`, update per-country premia.
6. **Audit log.** Append a row to §13 with date, inputs, computed values, retrieval URLs.
7. **Commit.** `K-Opp Index — <Month YYYY> refresh — <NNN> bps`. Push to `main` only after all guards pass.

The K-Opp number is **never** entered by hand into the JSON file. The JSON is the output of this procedure; if the procedure halts, the JSON does not change.

---

## 11. Method versioning

The method described above is **v1.0** (committed 2026-06-07).

Method changes (e.g. switching to GDP-weighted mean, changing a country's source table, adding a fifth country) require:

1. New version stamp in this file (v1.1, v2.0, …).
2. Written rationale in §14.
3. Recomputation of the full historical series under the new method, with the v1.0 series preserved alongside under a deprecation note.
4. Credit Note announcing the change with a side-by-side delta.

Number changes from input changes are **normal** and do not require a version bump.

---

## 12. Known limitations (declared on every issue)

1. **Source heterogeneity.** The four central banks publish different breakouts. Each proxy is named per-country in §3–§6.
2. **Vietnam priority-sector cap** mechanically suppresses the published premium; "Vietnam — uncapped" alternate planned for Q3 2026.
3. **IFC 2005 reference** is a single-vintage practitioner anchor, not a published index. The ladder of historical anchors will widen over the first four Credit Note issues (IFC 1995, EBRD 1998, etc.).
4. **FRED OAS series** (companion benchmarks, §8) are large-issuer indices; they are **not** SME spreads. They are the legible-market floor the K-Opp sits above. The contrast is the publication.
5. **Indonesia OJK premium** is published less frequently than the BI SEKI base rate. Between OJK publications, the premium is carried forward. This creates a one-sided drift: when corporate rates move, the SME proxy moves with them at the same magnitude, holding the spread constant until the next OJK update. This is acknowledged and is one of the reasons Indonesia is the lowest-volatility bar in the index.

---

## 13. Audit log (per-month inputs and outputs)

| Refresh date | Month | TH SME | TH CORP | PH SME | PH CORP | ID SME | ID CORP | VN SME | VN CORP | K-Opp (bps) | Method version | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 2026-06-07 | Jan 2026 | 8.91% | 4.15% | 11.30% | 5.90% | 11.41% | 8.06% | 9.70% | 7.40% | **395** | v1.0 | Reconstructed from `Credit-Notes-No01-The-Opacity-Premium-DRAFT` on methodology commit |

Backfill for the 18 prior months (Jul 2024 – Dec 2025) of the published series: **deferred** until a v1.0-conformant re-fetch can be done from primary sources for each month. The 19-month series currently rendered in Panel 02 is labelled as **back-tested under v1.0 method, primary-source re-fetch pending per-month audit log**. This is honest: the method is now documented; the historical reconciliation is the next audit work-item.

---

## 14. Method change rationale log

| Version | Date | Change | Rationale |
|---|---|---|---|
| v0.1 | 2026-06-07 (morning) | Initial skeleton committed | Filed against ISSUE-001. Skeleton had `MCR-INPUT-REQUIRED` placeholders in §3–§6 because the agent failed to extract the existing recipe from `Credit-Notes-No01-The-Opacity-Premium-DRAFT`. The recipe existed; it was not in the canonical file. |
| **v1.0** | 2026-06-07 (afternoon) | **Full method committed.** Recipes for §3 (Thailand), §4 (Philippines), §5 (Indonesia), §6 (Vietnam) lifted verbatim from Credit Notes Nº01 draft. Guards §9.1–§9.5 codified. Refresh procedure §10 specified. ISSUE-001 acceptance criteria (a)–(d) now satisfied; (e) refresh guard is encoded as §9 + §10. | The Credit Note is the editorial reading; this file is the canonical machine-readable recipe. They must not drift. |
