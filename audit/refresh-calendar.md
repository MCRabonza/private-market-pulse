# Refresh Calendar — pulse.krv.co

**Generated:** 2026-06-07 (WK23) · **Owner:** the agent · **Lives at:** `audit/refresh-calendar.md` on `main`

This is the single forward view of every scheduled change to pulse.krv.co. Six cadences, each owned by one cron. If a refresh is coming and it is not on this calendar, the cron roster is wrong, not the dashboard.

Paired with `references/cron-roster.md` (mechanism) and `audit/source-trace.md` (what each surface reads from).

---

## 1. Next 30 days — at a glance

| Date | Day | Surface | Cron | Status |
|---|---|---|---|---|
| **2026-06-07** | Sun | Source audit (37 URLs in `source-trace.md`) | `f305b474` source-audit-weekly | ✅ active (first fire tonight 22:00 ICT) |
| **2026-06-08** | Mon | Dateline → WK24 · JUNE 2026 | `2f203248` dateline-weekly | ✅ active |
| **2026-06-08** | Mon | Ribbon (10 live tickers, T−1) | `1716516a` ribbon-daily | ✅ active (email-on-fail wired) |
| **2026-06-08** | Mon | MPC release watch | `b1f6716e` mpc-watch | ✅ active |
| **2026-06-09** | Tue | Ribbon + MPC watch | ribbon-daily + mpc-watch | ✅ active |
| **2026-06-10** | Wed | Ribbon · BoT Monetary Policy Report publishes ([BoT MPC schedule](https://www.bot.or.th/en/our-roles/monetary-policy/mpc-meeting.html)) | ribbon-daily + mpc-watch | ✅ active |
| **2026-06-11** | Thu | Ribbon + MPC watch | ribbon-daily + mpc-watch | ✅ active |
| **2026-06-12** | Fri | Ribbon + MPC watch | ribbon-daily + mpc-watch | ✅ active |
| **2026-06-14** | Sun | Source audit | source-audit-weekly | ✅ active |
| **2026-06-15** | Mon | Ribbon + dateline → WK25 | ribbon-daily + dateline-weekly | ✅ active |
| **2026-06-17** | Wed | **FOMC rate decision** ([federalreserve.gov](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)) — mpc-watch drafts proposed ribbon policy update for MCR review | `b1f6716e` mpc-watch | ✅ active |
| **2026-06-17/18** | Wed/Thu | **Bank Indonesia RDG** ([bi.go.id](https://www.bi.go.id/en/publikasi/Kalender/Default.aspx)) — BI 4.75%, mpc-watch drafts update | mpc-watch | ✅ active |
| **2026-06-18** | Thu | **BSP Monetary Board** ([bsp.gov.ph](https://www.bsp.gov.ph/Pages/PriceStability/ScheduleOfMeetingsOfTheAdvisoryCommitteeAndMonetaryBoardOnMonetaryPolicy.aspx)) — BSP 4.25%, mpc-watch drafts update | mpc-watch | ✅ active |
| **2026-06-21** | Sun | Source audit | source-audit-weekly | ✅ active |
| **2026-06-22** | Mon | Ribbon + dateline → WK26 | ribbon-daily + dateline-weekly | ✅ active |
| **2026-06-24** | Wed | **Bank of Thailand MPC** ([BoT MPC schedule](https://www.bot.or.th/en/our-roles/monetary-policy/mpc-meeting.html)) — BoT 1.00%, mpc-watch drafts update | mpc-watch | ✅ active |
| **2026-06-28** | Sun | Source audit | source-audit-weekly | ✅ active |
| **2026-06-29** | Mon | Ribbon + dateline → WK27 | ribbon-daily + dateline-weekly | ✅ active |
| **2026-07-01** | Wed | **K-Opp Index monthly refresh** (Jul 2026 print) — first business day, methodology §10, 5 guards | `dfe2d955` kopp-monthly | ✅ active |
| **2026-07-01** | Wed | **Section quarterly draft branch opens** (Q3 2026 — Sections 03–08 re-source) | `8bf1f59f` section-quarterly | ✅ active |

---

## 2. Cron roster — current cadence and status

| # | Cron ID | Cron | Cadence (ICT) | Surface written | Next fire | Status |
|---|---|---|---|---|---|---|
| 1 | `1716516a` | ribbon-daily | Mon–Fri 07:00 | `data/ribbon-data.json` (10 live items) | Mon 2026-06-08 07:00 ICT | ✅ active (email-on-fail wired 2026-06-07) |
| 2 | `2f203248` | dateline-weekly | Mon 06:55 | `data/dateline.json` | Mon 2026-06-08 06:55 ICT | ✅ active |
| 3 | `dfe2d955` | kopp-monthly | 1st biz day 08:00 (programmatic trigger) | `data/k-opp-series.json` + `audit/k-opp-methodology.md` §13 | Wed 2026-07-01 08:00 ICT | ✅ active (v1.0 methodology, 5 guards) |
| 4 | `8bf1f59f` | section-quarterly | Q1/Q2/Q3/Q4 1st 09:00 | branch `pulse/quarterly-draft-YYYYQN` | Wed 2026-07-01 09:00 ICT | ✅ active (draft-only, never commits to main) |
| 5 | `f305b474` | source-audit-weekly | Sun 22:00 | `audit/source-health.json` | **Sun 2026-06-07 22:00 ICT (tonight)** | ✅ active |
| 6 | `b1f6716e` | mpc-watch | Mon–Fri 07:30 | `data/ribbon-data.json` policy items | Mon 2026-06-08 07:30 ICT | ✅ active (MCR-approval-gated) |

**6 of 6 crons live as of 2026-06-07.** Every refresh is now owned. Manual intervention required only for: (a) section-quarterly PR merges, (b) mpc-watch policy-rate change approvals, (c) any cron failure (email on fail wired for all six).

---

## 3. Quarterly milestones — Q3 2026 (Jul 1 – Sep 30)

| Date | Event | Touches | Cron |
|---|---|---|---|
| 2026-07-01 | K-Opp July print | Section 01 headline, 19-month series | `dfe2d955` |
| 2026-07-01 | Q3 section refresh draft branch opens | Sections 03–08 (Thailand, rate paradox, regional pattern, capital, inheritance, accountancy) | `8bf1f59f` |
| 2026-07-21/22 | Bank Indonesia RDG | Ribbon BI policy rate | `b1f6716e` |
| 2026-07-23 | BSP Monetary Board | Ribbon BSP policy rate | `b1f6716e` |
| 2026-07-28/29 | FOMC | Ribbon US 10Y reaction; companion FRED series for K-Opp benchmarks | `b1f6716e` |
| 2026-08-05 | BoT Monetary Policy Report (April meeting follow-up) | Section 03/04 Thailand context | manual |
| 2026-08-18/19 | Bank Indonesia RDG | Ribbon BI policy rate | `b1f6716e` |
| 2026-08-26 | Bank of Thailand MPC | Ribbon BoT policy rate | `b1f6716e` |
| 2026-08-27 | BSP Monetary Board | Ribbon BSP policy rate | `b1f6716e` |
| 2026-09-15/16 | FOMC (with SEP) | Ribbon US 10Y | `b1f6716e` |
| 2026-09-22/23 | Bank Indonesia RDG | Ribbon BI policy rate | `b1f6716e` |

**Sources for the schedule:** [BoT MPC](https://www.bot.or.th/en/our-roles/monetary-policy/mpc-meeting.html) · [BI Kalender](https://www.bi.go.id/en/publikasi/Kalender/Default.aspx) · [BSP MB Calendar](https://www.bsp.gov.ph/Pages/PriceStability/ScheduleOfMeetingsOfTheAdvisoryCommitteeAndMonetaryBoardOnMonetaryPolicy.aspx) · [FOMC](https://www.federalreserve.gov/aboutthefed/boardmeetings/meetingdates.htm). SBV does not publish a fixed MPC calendar — `mpc-watch` polls [vnba.org.vn](https://vnba.org.vn) and [sbv.gov.vn](https://sbv.gov.vn) daily.

---

## 4. Audit-pending work-items (independent of crons)

These are work items the agent will close session-by-session as MCR approves. They do not need a cron — they need authoring time.

| ID | Surface | Status |
|---|---|---|
| ISSUE-001 | K-Opp methodology + source trace (Section 01) | **CLOSED 2026-06-07** — see §5 |
| ISSUE-002 | Cost stack methodology (Section 04 — 9.5–13.5% breakdown) | **CLOSED 2026-06-07** — see §6 |
| Section 02 source trace (7 rows) | `audit/source-trace.md` §2 | Pending re-fetch — IFC SME Finance Forum + ADB Asia SME Monitor |
| Section 03 source trace (6 rows) | §3 Thailand | Pending re-fetch — OSMEP, TFAC, BoT FSR |
| Section 05 source trace (8 rows) | §5 regional pattern | Pending re-fetch — OJK, BSP Magna Carta, GSO, EuroCham BCI |
| Section 06–07 source trace (7 rows) | §6–7 accountancy gap | Pending re-fetch — TFAC, PICPA, IAI, VAA, OECD |
| Section 01b (EM credit yield compilation) | `section-reaching` | Not built — pending MCR go-signal per `PULSE_MASTER_PROMPT.md` §2.2 |

Note: Section 02–07 re-fetches are now owned by `8bf1f59f` section-quarterly starting Q3 2026 (1 Jul 2026). They will land as a draft branch for MCR review, not as ad-hoc work.

---

## 5. ISSUE-001 closure

**Filed:** 2026-06-07 by COO. **Closed:** 2026-06-07.

| Acceptance criterion | Evidence |
|---|---|
| (a) Single written definition matches rendered headline | `audit/k-opp-methodology.md` §1 — *"ASEAN-4 SME-vs-corporate raw lending spread, simple arithmetic mean across {TH, PH, ID, VN}, in basis points."* Reconciles to 395 bps. |
| (b) Methodology reproduces 540/476/335/230 and 395 from cited primary sources | k-opp-methodology.md §3–§7. (540+476+335+230)/4 = 395.25 → 395. ✅ |
| (c) `audit/source-trace.md` exists with primary URL + retrieval date for Section 01 | source-trace.md §1, all 11 K-Opp rows now **Verified** on commit `bc369d2`. ✅ |
| (d) `PULSE_MASTER_PROMPT.md` no longer contains contradicting formula | §2.1 patched 2026-06-07 — *"Not policy rate minus Fed Funds. That earlier formulation was a labelling error in this file; it was corrected on 2026-06-07 against ISSUE-001."* Skill re-saved. ✅ |
| (e) Refresh guard documented so headline cannot be auto-recomputed without method-match | k-opp-methodology.md §9–§10 + `pulse-living-maintenance/references/kopp-refresh-runbook.md` v1.0 (5 guards + 8-step procedure). Skill re-saved. ✅ |

**Audit trail on `main`:** commits `4b97678` (skeletons) → `f120ca5` (methodology v1.0) → `bc369d2` (source-trace §1 verified).

**Bonus closure:** Cron 3 (`dfe2d955` kopp-monthly) created 2026-06-07 carries the v1.0 methodology verbatim — every monthly print is now method-guarded.

---

## 6. ISSUE-002 closure

**Filed:** 2026-06-07 by COO (self-caught after MCR sent screenshot of live Section 04 cost-decomposition panel). **Closed:** 2026-06-07.

Same drift pattern as ISSUE-001: the cost stack recipe was already methodologised on the live dashboard (Section 04 panel renders the 4 layers + total), but never extracted to `audit/`. The fix was to extract the recipe verbatim from the live render into an authoritative methodology file and verify the source-trace §4 row.

| Acceptance criterion | Evidence |
|---|---|
| (a) Single written definition matches rendered headline | `audit/cost-stack-methodology.md` §1 — *"TOTAL_COST_TO_EXTEND = Operating(3.0–4.0%) + Provisioning(2.5–4.0%) + Cost_of_Funds(2.5–3.5%) + Basel_III(1.5–2.0%) = 9.5–13.5%"* Reconciles to Section 04 panel. |
| (b) Each layer reproduces from cited primary source | cost-stack-methodology.md §2 (Operating, IFC SME Banking Knowledge Guide + KRV practitioner) · §3 (Provisioning, [BoT FS Review Q3 2025](https://www.bot.or.th/en/research-and-publications/articles-and-publications/financial-stability-report.html)) · §4 (Cost of Funds, BoT FM_RT_001 series) · §5 (Basel III, [BIS Basel III](https://www.bis.org/bcbs/basel3.htm) + [BoT capital adequacy framework](https://www.bot.or.th/en/financial-institutions/key-regulations/capital-adequacy.html)). ✅ |
| (c) `audit/source-trace.md` §4 Verified for cost stack row | source-trace.md §4 — risk weight, cost stack, yield, negative spread all flipped to **Verified** on commit `cb17bbb`. ✅ |
| (d) Downstream negative spread arithmetic documented | Yield 8–10% − Cost 9.5–13.5% = −1% to −5% net. Section 04 prose reads −2.5% midpoint. ✅ |
| (e) Refresh guard documented | cost-stack-methodology.md §9 — 5-guard structure parallel to K-Opp methodology. Next refresh: `8bf1f59f` section-quarterly Q3 2026 (1 Jul 2026). ✅ |

**Audit trail on `main`:** commit `cb17bbb` (cost-stack-methodology.md v1.0 + source-trace.md §4 verified).

---

## 7. How to read this calendar

- **Today is 2026-06-07.** The calendar is regenerated on every Pulse session that touches a refresh surface.
- **A row marked ✅ active** means the cron exists, is wired to a notification channel (email on failure), and will fire on its next scheduled tick.
- **If a date in §1 passes without the corresponding cron firing,** check the cron's last_run via `pplx-tool schedule_cron action=list` and the email inbox for failure notifications. The recovery playbook is in `pulse-living-maintenance` §4.
- **No row gets silently dropped.** This file is the audit trail of what was promised vs what happened.
