# K-Opp Index — Methodology

**Status:** v0.1 · skeleton committed to make the methodology gap visible on `main`
**Owner:** MCR (method) · agent (computation, rendering, audit trail)
**Last updated:** 2026-06-07
**Filed against:** ISSUE-001 — The K-Opp headline is not reproducible from its stated methodology

---

## 0. Statement of intent

The K-Opp Index is a published measurement. Its authority is computational, not editorial. The method below defines the index. The number is whatever the method produces from honest, primary-sourced inputs. The number is not set by preference. The method is set by MCR, once, and revised only with version control and a written rationale.

If on any future refresh the method produces a value MCR finds inconvenient, the resolution is one of:
(a) the inputs are wrong — re-fetch and recompute,
(b) the method is wrong — propose a v0.2, write the rationale, version the change,
(c) the answer is the news — publish a Credit Note explaining the regime shift.

The resolution is never (d) overwrite the headline with a preferred number. That option does not exist.

---

## 1. Canonical definition

**K-Opp Index** = the ASEAN-4 SME-vs-corporate simple-mean lending spread, in basis points.

For each of the four ASEAN-4 countries (Thailand, Philippines, Indonesia, Vietnam), compute a country-level **SME risk premium**: the spread between the weighted-average lending rate to SMEs and the weighted-average lending rate to large corporates, expressed in basis points. The K-Opp Index is the arithmetic mean of the four country premia.

```
K-Opp (bps) = round( ( SME_premium_TH + SME_premium_PH + SME_premium_ID + SME_premium_VN ) / 4 )

  where  SME_premium_<country> (bps) = round( ( SME_lending_rate − Corporate_lending_rate ) × 100 )
```

The four country premia are published as **Panel 03 — Country Ladder**. The K-Opp Index is the headline (Section 01 hero stat).

**Current values (as of January 2026, the live publication):**

| Country | SME premium (bps) | Status |
|---|---|---|
| Philippines | 540 | MCR-INPUT-REQUIRED — assembly not documented |
| Thailand    | 476 | MCR-INPUT-REQUIRED — assembly not documented |
| Indonesia   | 335 | MCR-INPUT-REQUIRED — assembly not documented |
| Vietnam     | 230 | MCR-INPUT-REQUIRED — priority-cap distortion netting not documented |
| **Mean (K-Opp)** | **395** | Reproduces from the four bars to the digit: (540+476+335+230)/4 = 395.25 → 395 |

The headline reconciles to the four bars. What is not yet documented is **how each of the four bars is constructed from primary data**. Until §3–§6 are filled, the index is auditable at the aggregation step (§7) but not at the country-construction step.

---

## 2. Cadence and anchoring

- **Refresh cadence:** monthly, on the first business day of each calendar month, reflecting the most recently completed month's data.
- **Anchor date:** month-end of the prior calendar month (e.g. June 1 refresh uses May 31 data).
- **Carry-forward rule:** if a country's source data is not yet published by month-end + 5 business days, the prior month's value carries forward with an explicit annotation in the audit log. Carry-forward beyond 60 days requires MCR review.

---

## 3. Thailand SME premium — construction

> **STATUS: MCR-INPUT-REQUIRED.** The current bar (476 bps) was built during the original Pulse construction; the recipe was not written down. The fields below are the questions the recipe must answer.

| Field | Value | Source |
|---|---|---|
| SME contract-size band | _MCR-INPUT-REQUIRED_ (e.g. ≤ 50M THB? ≤ 100M THB? aligned to BoT SME definition?) | _MCR-INPUT-REQUIRED_ |
| SME lending rate source | _MCR-INPUT-REQUIRED_ (BoT weighted-average lending rate by loan-size band? Commercial bank survey?) | _MCR-INPUT-REQUIRED_ |
| Corporate lending rate source | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Frequency | _MCR-INPUT-REQUIRED_ (monthly? quarterly with monthly interpolation?) | _MCR-INPUT-REQUIRED_ |
| Computation | `SME_rate − Corporate_rate`, expressed in bps | — |
| Current month value | 476 bps (January 2026) | _MCR-INPUT-REQUIRED_ |
| Primary URL | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Retrieval date | _MCR-INPUT-REQUIRED_ | — |

---

## 4. Philippines SME premium — construction

> **STATUS: MCR-INPUT-REQUIRED.** Current bar 540 bps.

| Field | Value | Source |
|---|---|---|
| SME contract-size band | _MCR-INPUT-REQUIRED_ (Magna Carta SME definition? BSP SLS contract-size band?) | _MCR-INPUT-REQUIRED_ |
| SME lending rate source | _MCR-INPUT-REQUIRED_ (BSP Senior Loan Officers' Survey? BSP MSME finance statistics?) | _MCR-INPUT-REQUIRED_ |
| Corporate lending rate source | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Frequency | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Computation | `SME_rate − Corporate_rate`, expressed in bps | — |
| Current month value | 540 bps (January 2026) | _MCR-INPUT-REQUIRED_ |
| Primary URL | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Retrieval date | _MCR-INPUT-REQUIRED_ | — |

---

## 5. Indonesia SME premium — construction

> **STATUS: MCR-INPUT-REQUIRED.** Current bar 335 bps. Skill canon refers to a "SEKI + OJK MSME premium" assembly; the actual formula is not documented.

| Field | Value | Source |
|---|---|---|
| SME contract-size band | _MCR-INPUT-REQUIRED_ (BI/OJK MSME definition? IDR-denominated band?) | _MCR-INPUT-REQUIRED_ |
| SME lending rate source — component A | _MCR-INPUT-REQUIRED_ (BI SEKI — which table?) | _MCR-INPUT-REQUIRED_ |
| SME lending rate source — component B | _MCR-INPUT-REQUIRED_ (OJK MSME premium — which release?) | _MCR-INPUT-REQUIRED_ |
| Assembly formula | _MCR-INPUT-REQUIRED_ (how A and B combine — additive? weighted? max?) | — |
| Corporate lending rate source | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Frequency | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Current month value | 335 bps (January 2026) | _MCR-INPUT-REQUIRED_ |
| Primary URL(s) | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Retrieval date | _MCR-INPUT-REQUIRED_ | — |

---

## 6. Vietnam SME premium — construction

> **STATUS: MCR-INPUT-REQUIRED.** Current bar 230 bps, flagged in canon as "priority-cap distorted, top–bottom of range."

| Field | Value | Source |
|---|---|---|
| SME contract-size band | _MCR-INPUT-REQUIRED_ (SBV SME classification?) | _MCR-INPUT-REQUIRED_ |
| Raw observed SME-vs-corp spread | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Priority-cap distortion magnitude | _MCR-INPUT-REQUIRED_ (the cap-induced compression that needs to be netted out) | _MCR-INPUT-REQUIRED_ |
| Netting formula | _MCR-INPUT-REQUIRED_ (how the priority-cap distortion is backed out — multiplicative? additive? from disclosed range?) | — |
| Resulting "true" SME premium | 230 bps (January 2026) | _MCR-INPUT-REQUIRED_ |
| Frequency | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Primary URL(s) | _MCR-INPUT-REQUIRED_ | _MCR-INPUT-REQUIRED_ |
| Retrieval date | _MCR-INPUT-REQUIRED_ | — |

---

## 7. Aggregation rule

```
K-Opp (bps) = round_half_up( ( SME_premium_TH + SME_premium_PH + SME_premium_ID + SME_premium_VN ) / 4 )
```

- Simple arithmetic mean. **No GDP-weighting, no banking-sector-size weighting.** A simple mean treats each ASEAN-4 economy as one observation in the same regional accountancy/credit-gap regime. If MCR later wants GDP-weighting, that is a v0.2 method change and is versioned.
- Rounding: half-up to the nearest integer basis point.
- Headline reconciliation: the published `headline_bps` in `data/k-opp-series.json` must equal this computation to the digit. The renderer enforces this (see §9).

---

## 8. Guards (the index cannot be set by preference)

### 8.1 Reproducibility guard

A refresh is accepted only if `round((SME_TH + SME_PH + SME_ID + SME_VN) / 4) == headline_bps` to the digit. If the four bars do not reconcile to the headline, neither the bars nor the headline are written. The refresh halts and emails MCR with the discrepancy.

### 8.2 Discontinuity guard

If `|new_K-Opp − prior_K-Opp| > 50 bps`, the refresh halts and emails MCR with the per-country breakdown. A move >50 bps is either a genuine regime shift (worth a Credit Note, not a silent refresh) or an input error. Either way, MCR confirms before commit.

### 8.3 Sign and range guard

Each country premium must be in `[0, 2000]` bps (0 to 20 percentage points). A negative spread would mean SMEs borrow cheaper than large corporates, which is implausible under the ASEAN regulatory regime; >2000 bps would mean a >20pp spread, which would be a national crisis worth its own Credit Note. Either triggers a halt.

### 8.4 No-override rule

The K-Opp number cannot be set by hand. The renderer reads `data/k-opp-series.json`; the JSON file is written only by the monthly refresh procedure described in §10. If MCR wants to override, the override changes the method (versioned, §11), not the number.

---

## 9. Rendering contract (`index.html` ↔ `data/k-opp-series.json`)

The dashboard reads `data/k-opp-series.json` on page load via `renderKopp()` (lines ~1410–1614 of `index.html`). The renderer:

- Sets `[data-kopp-headline]` text to `${headline_bps} bps`.
- Draws the five Panel 02 series paths from `series.{asean4, us_hyig, em_corp, asia_em, fedfunds}`.
- Draws Panel 03 bars from a future `country_premia` block in the JSON (not yet wired — see §12).

**Naming defect (open):** the series currently stored as `series.asean4` in `data/k-opp-series.json` is the **time-series of the K-Opp Index itself** (`headline_bps` history), not a series of policy rates. The variable name is misleading and will be renamed to `series.kopp_index` in the next schema bump (v1.1).

---

## 10. Refresh procedure (monthly, first business day)

1. **Inputs.** Fetch each country's SME lending rate and corporate lending rate from the primary sources documented in §3–§6.
2. **Per-country computation.** For each country: `SME_premium_<country> = round( (SME_rate − Corporate_rate) × 100 )` in bps. Apply the country-specific netting rule (Indonesia §5 assembly; Vietnam §6 priority-cap netting).
3. **Aggregation.** `K-Opp = round_half_up( sum(SME_premia) / 4 )`.
4. **Guards.** Run §8.1 (reproducibility), §8.2 (discontinuity), §8.3 (sign/range). Any halt blocks the commit and notifies MCR.
5. **Write.** Append to `data/k-opp-series.json`: extend `months[]`, extend `series.kopp_index[]`, update `headline_bps` and `headline_label`. Update `country_premia` for the new month.
6. **Audit log.** Append a row to this file's §13 with date, inputs, computed values, and primary URLs.
7. **Commit.** Single commit `K-Opp Index — <Month YYYY> refresh — <NNN> bps`. Push to `main` only after guards pass.

**No step in this procedure permits hand-setting the headline.**

---

## 11. Method versioning

The method described in §1, §7, §8 is version **v0.1**. Method changes (e.g. switching from simple mean to GDP-weighted mean; changing the SME contract-size band in a country; changing the rounding rule) require:

1. A new version stamp in this file (v0.2, v0.3, ...).
2. A written rationale committed to this file's §14.
3. Recomputation of the full historical series under the new method, with the old series preserved alongside under a deprecation note.
4. A Credit Note announcing the method change to readers, with the side-by-side delta.

Method changes are rare. Numbers changing because inputs changed are normal and require no version bump.

---

## 12. Open items (pre-acceptance criteria for ISSUE-001)

- [ ] §3 Thailand SME premium recipe filled
- [ ] §4 Philippines SME premium recipe filled
- [ ] §5 Indonesia SME premium recipe filled
- [ ] §6 Vietnam SME premium recipe filled
- [ ] `data/k-opp-series.json` schema v1.1: rename `series.asean4` → `series.kopp_index`; add `country_premia` block with monthly history per country
- [ ] `renderKopp()` updated to read renamed key with backward-compat fallback
- [ ] §13 audit log backfilled for the 19 months currently in the series (or marked "pre-method-doc, reconstructed from publication")
- [ ] `PULSE_MASTER_PROMPT.md` §2.1 patched to delete the policy-minus-Fed formula and point here
- [ ] `pulse-living-maintenance` skill `references/kopp-refresh-runbook.md` rewritten to match this method (currently codifies the wrong formula)

---

## 13. Audit log (per-month inputs and outputs)

| Refresh date | Month | TH SME | PH SME | ID SME | VN SME | K-Opp (bps) | Method version | Sources |
|---|---|---|---|---|---|---|---|---|
| Jan 2026 | Jan 2026 | 476 | 540 | 335 | 230 | 395 | v0.1 (skeleton) | _pre-method-doc, reconstructed from publication_ |

Rows backfilled for prior months: deferred until §3–§6 are filled and the historical series can be recomputed under the documented method. Until then, the 19-month `kopp_index` series stored in `data/k-opp-series.json` is **labelled as reconstructed**, not as recomputed.

---

## 14. Method change rationale log

| Version | Date | Change | Rationale |
|---|---|---|---|
| v0.1 | 2026-06-07 | Skeleton committed | ISSUE-001: prior canon documented a formula (mean policy − Fed) that did not produce the published headline. This file establishes the canonical definition (SME-vs-corporate spread, simple mean) and exposes the four country recipes as MCR-input-required. |
