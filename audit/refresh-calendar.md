# Refresh Calendar — pulse.krv.co

**Generated:** 2026-06-07 (WK23) · **Owner:** the agent · **Lives at:** `audit/refresh-calendar.md` on `main`

This is the single forward view of every scheduled change to pulse.krv.co. Six cadences, each owned by one cron. If a refresh is coming and it is not on this calendar, the cron roster is wrong, not the dashboard.

Paired with `references/cron-roster.md` (mechanism) and `audit/source-trace.md` (what each surface reads from).

---

## 1. Next 30 days — at a glance

| Date | Day | Surface | Cron | Status |
|---|---|---|---|---|
| **2026-06-08** | Mon | Ribbon (10 live tickers, T−1) | `1716516a` ribbon-daily | ✅ active |
| **2026-06-08** | Mon | Dateline → WK24 · JUNE 2026 | `dateline-weekly` | ⏳ cron not yet created |
| **2026-06-09** | Tue | Ribbon | ribbon-daily | ✅ active |
| **2026-06-10** | Wed | Ribbon · BoT Monetary Policy Report publishes ([BoT MPC schedule](https://www.bot.or.th/en/our-roles/monetary-policy/mpc-meeting.html)) | ribbon-daily | ✅ active |
| **2026-06-11** | Thu | Ribbon | ribbon-daily | ✅ active |
| **2026-06-12** | Fri | Ribbon | ribbon-daily | ✅ active |
| **2026-06-14** | Sun | Source audit (37 pending URLs) | `source-audit-weekly` | ⏳ cron not yet created |
| **2026-06-15** | Mon | Ribbon + dateline → WK25 | ribbon-daily + dateline-weekly | partial |
| **2026-06-17** | Wed | **FOMC rate decision** ([federalreserve.gov](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)) — ribbon US 10Y reacts, agent may need to draft policy-rate change for K-Opp companion data | `mpc-watch` | ⏳ cron not yet created |
| **2026-06-17/18** | Wed/Thu | **Bank Indonesia RDG** ([bi.go.id](https://www.bi.go.id/en/publikasi/Kalender/Default.aspx)) — BI policy rate currently 4.75%, agent must draft ribbon update if changed | mpc-watch | ⏳ cron not yet created |
| **2026-06-18** | Thu | **BSP Monetary Board** ([bsp.gov.ph](https://www.bsp.gov.ph/Pages/PriceStability/ScheduleOfMeetingsOfTheAdvisoryCommitteeAndMonetaryBoardOnMonetaryPolicy.aspx)) — BSP policy rate currently 4.25%, agent must draft ribbon update if changed | mpc-watch | ⏳ cron not yet created |
| **2026-06-22** | Mon | Ribbon + dateline → WK26 | ribbon-daily + dateline-weekly | partial |
| **2026-06-24** | Wed | **Bank of Thailand MPC** ([BoT MPC schedule](https://www.bot.or.th/en/our-roles/monetary-policy/mpc-meeting.html)) — BoT policy rate currently 1.00%, agent must draft ribbon update if changed | mpc-watch | ⏳ cron not yet created |
| **2026-06-29** | Mon | Ribbon + dateline → WK27 | partial | |
| **2026-07-01** | Wed | **K-Opp Index monthly refresh** (Jul 2026 print) — first business day, per methodology §10 | `kopp-monthly` | ⏳ cron not yet created |
| **2026-07-01** | Wed | **Section quarterly draft branch opens** (Q3 2026 cycle — Sections 02–07 re-source) | `section-quarterly` | ⏳ cron not yet created |

---

## 2. Cron roster — current cadence and status

| # | Cron | Cadence (ICT) | Surface written | Next fire | Status |
|---|---|---|---|---|---|
| 1 | ribbon-daily (`1716516a`) | Mon–Fri 07:00 | `data/ribbon-data.json` (10 live items) | **Mon 2026-06-08 07:00 ICT** | ✅ active |
| 2 | dateline-weekly | Mon 06:55 | `data/dateline.json` | Mon 2026-06-08 06:55 ICT | ⏳ DENIED — needs MCR approval |
| 3 | kopp-monthly | 1st biz day 08:00 | `data/k-opp-series.json` | **Wed 2026-07-01 08:00 ICT** | ⏳ DENIED — needs MCR approval |
| 4 | section-quarterly | Jan/Apr/Jul/Oct 1st 09:00 | branch `pulse/quarterly-draft-YYYYQN` | **Wed 2026-07-01 09:00 ICT** | ⏳ DENIED — needs MCR approval |
| 5 | source-audit-weekly | Sun 22:00 | `audit/source-health.json` | **Sun 2026-06-14 22:00 ICT** | ⏳ DENIED — needs MCR approval |
| 6 | mpc-watch | Mon–Fri 07:30 + programmatic | `data/ribbon-data.json` policy items (BoT/BSP/BI/SBV) | next FOMC/BI Wed 2026-06-17 | ⏳ DENIED — needs MCR approval |

**Today only 1 of 6 crons is live.** Five cadences are documented in `pulse-living-maintenance/references/cron-roster.md` but not running. Until they are approved, every refresh outside the ribbon is manual.

---

## 3. Quarterly milestones — Q3 2026 (Jul 1 – Sep 30)

| Date | Event | Touches |
|---|---|---|
| 2026-07-01 | K-Opp July print | Section 01 headline, 19-month series |
| 2026-07-01 | Q3 section refresh draft branch opens | Sections 02–07 (defining problem, Thailand, rate paradox, regional pattern, accountancy gap) — primary-source re-fetch per `section-quarterly-runbook.md` |
| 2026-07-21/22 | Bank Indonesia RDG (mid-quarter) | Ribbon BI policy rate |
| 2026-07-23 | BSP Monetary Board | Ribbon BSP policy rate |
| 2026-07-28/29 | FOMC | Ribbon US 10Y reaction; companion FRED series for K-Opp benchmarks |
| 2026-08-05 | BoT Monetary Policy Report (April meeting follow-up) | Section 03/04 Thailand context |
| 2026-08-18/19 | Bank Indonesia RDG | Ribbon BI policy rate |
| 2026-08-26 | Bank of Thailand MPC | Ribbon BoT policy rate |
| 2026-08-27 | BSP Monetary Board | Ribbon BSP policy rate |
| 2026-09-15/16 | FOMC (with SEP) | Ribbon US 10Y |
| 2026-09-22/23 | Bank Indonesia RDG | Ribbon BI policy rate |

**Sources for the schedule:** [BoT MPC](https://www.bot.or.th/en/our-roles/monetary-policy/mpc-meeting.html) · [BI Kalender](https://www.bi.go.id/en/publikasi/Kalender/Default.aspx) · [BSP MB Calendar](https://www.bsp.gov.ph/Pages/PriceStability/ScheduleOfMeetingsOfTheAdvisoryCommitteeAndMonetaryBoardOnMonetaryPolicy.aspx) · [FOMC](https://www.federalreserve.gov/aboutthefed/boardmeetings/meetingdates.htm). SBV does not publish a fixed MPC calendar — the agent watches [vnba.org.vn](https://vnba.org.vn) and [sbv.gov.vn](https://sbv.gov.vn) monthly.

---

## 4. Audit-pending work-items (independent of crons)

These are work items the agent will close session-by-session as MCR approves. They do not need a cron — they need authoring time.

| ID | Surface | Status |
|---|---|---|
| ISSUE-001 | K-Opp methodology + source trace (Section 01) | **CLOSED 2026-06-07** — see §5 |
| Section 02 source trace (7 rows) | `audit/source-trace.md` §2 | Pending re-fetch — IFC SME Finance Forum + ADB Asia SME Monitor |
| Section 03 source trace (6 rows) | §3 Thailand | Pending re-fetch — OSMEP, TFAC, BoT FSR |
| Section 04 source trace (5 rows) | §4 rate paradox | Pending — KRV cost stack methodology PDF (MCR input required for the 9.5–13.5% breakdown only) |
| Section 05 source trace (8 rows) | §5 regional pattern | Pending re-fetch — OJK, BSP Magna Carta, GSO, EuroCham BCI |
| Section 06–07 source trace (7 rows) | §6–7 accountancy gap | Pending re-fetch — TFAC, PICPA, IAI, VAA, OECD |
| Section 04 (k-opp companion HY/IG/EM OAS chart) | Section 01 Panel 02 | Charts render Chart.js; source trace verified, no work outstanding |
| Section 01b (EM credit yield compilation) | `section-reaching` | Not built — pending MCR go-signal per `PULSE_MASTER_PROMPT.md` §2.2 |

---

## 5. ISSUE-001 closure

**Filed:** 2026-06-07 by COO. **Closed:** 2026-06-07.

| Acceptance criterion | Evidence |
|---|---|
| (a) Single written definition matches rendered headline | `audit/k-opp-methodology.md` §1 — *"ASEAN-4 SME-vs-corporate raw lending spread, simple arithmetic mean across {TH, PH, ID, VN}, in basis points."* Reconciles to 395 bps. |
| (b) Methodology reproduces 540/476/335/230 and 395 from cited primary sources | k-opp-methodology.md §3–§7. (540+476+335+230)/4 = 395.25 → 395. ✅ |
| (c) `audit/source-trace.md` exists with primary URL + retrieval date for Section 01 | source-trace.md §1, all 11 K-Opp rows now **Verified** on commit `bc369d2`. ✅ |
| (d) `PULSE_MASTER_PROMPT.md` no longer contains contradicting formula | §2.1 patched 2026-06-07 — *"Not policy rate minus Fed Funds. That earlier formulation was a labelling error in this file; it was corrected on 2026-06-07 against ISSUE-001."* Skill re-saved (`krv-private-market-pulse` v1.x). ✅ |
| (e) Refresh guard documented so headline cannot be auto-recomputed without method-match | k-opp-methodology.md §9–§10 + `pulse-living-maintenance/references/kopp-refresh-runbook.md` v1.0 (5 guards + 8-step procedure). Skill re-saved. ✅ |

**Audit trail on `main`:** commits `4b97678` (skeletons) → `f120ca5` (methodology v1.0) → `bc369d2` (source-trace §1 verified).

---

## 6. How to read this calendar

- **Today is 2026-06-07.** The calendar is regenerated on every Pulse session that touches a refresh surface.
- **A row marked ⏳ cron not yet created** means the cadence is defined but no `schedule_cron` task has been created. The cron roster in `pulse-living-maintenance/references/cron-roster.md` has the exact `schedule_cron` payload for each one.
- **If a date in §1 passes without the corresponding ⏳ task firing,** the agent must either (a) run that refresh manually that session, or (b) explicitly defer it with reason logged here.
- **No row gets silently dropped.** This file is the audit trail of what was promised vs what happened.
