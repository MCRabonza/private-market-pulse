# KRV & Co. — Private Market Pulse

**Live ASEAN SME Intelligence Dashboard**
`pulse.krv.co` · KRV & Co. · Confidential · 2026

---

## What This Is

A live, publicly accessible data dashboard covering the structural SME credit gap across ASEAN's four highest-growth markets: Thailand, Philippines, Indonesia, and Vietnam.

Four charts, updated on a rolling basis from primary institutional sources.

---

## Dashboard Sections

| Section | Chart | Description |
|---|---|---|
| // 01 | **Chart A — SME Funding Gap** | Absolute USD gap + Gap as % of GDP vs. EM average |
| // 02 | **Chart B — SME Lending Volume** | SME credit share + YoY growth vs. peers |
| // 03 | **Chart C — Lending Cost vs. Rate** | Cost anatomy (4 layers) + Rate Paradox timeline 2019–2026 |
| // 04 | **Chart D — CPA Capacity** | CPAs per 1,000 SMEs · speedometer gauges by country |

---

## Data Sources & Update Cadence

| Pillar | Source | Cadence |
|---|---|---|
| SME Funding Gap | [IFC MSME Finance Gap Report](https://www.smefinanceforum.org/) | Annual (Apr–May) |
| SME Funding Gap | [World Bank Financial Sector Data](https://data.worldbank.org/) | Annual |
| SME Funding Gap | [ADB Asia SME Monitor](https://aric.adb.org/) | Annual |
| Lending Volume (Thailand) | [Bank of Thailand](https://www.bot.or.th/en/financial-institutions.html) | Monthly |
| Lending Volume (Philippines) | [Bangko Sentral ng Pilipinas](https://www.bsp.gov.ph/) | Quarterly |
| Lending Volume (Indonesia) | [Bank Indonesia](https://www.bi.go.id/) | Monthly |
| Lending Volume (Vietnam) | [State Bank of Vietnam](https://www.sbv.gov.vn/) | Quarterly |
| Policy Rate | [BOT Monetary Policy](https://www.bot.or.th/en/monetary-policy.html) | Per MPC meeting (~6×/year) |
| Lending Rates / NIM | [BIS Statistics](https://www.bis.org/statistics/) | Quarterly |
| NPL / Financial Soundness | [IMF FSI](https://www.imf.org/en/Data) | Quarterly |
| CPA Registry (Thailand) | [FAP Thailand](https://www.fap.or.th/) | Annual |
| CPA Registry (Regional) | [IFAC Global Accountancy Report](https://www.ifac.org/) | Annual |
| SME Registration (Thailand) | [OSMEP](https://www.sme.go.th/) | Annual |
| SME Registration (Philippines) | [DTI Philippines](https://www.dti.gov.ph/) | Annual |
| SME Registration (Indonesia) | [BPS / Kadin](https://www.bps.go.id/) | Annual |

---

## How to Update Data

All chart data is currently hardcoded in `index.html` inside the `<script>` block at the bottom of the file. To update:

1. Open `index.html`
2. Find the relevant chart data array (each chart is clearly labeled with a comment e.g. `// ── CHART A — FUNDING GAP`)
3. Update the values
4. Commit and push — GitHub Pages deploys automatically within ~60 seconds

**Future:** Data will be migrated to `/data/*.json` files so non-technical team members can update numbers without touching code.

---

## Deployment

- **Hosting:** GitHub Pages (`MCRabonza/private-market-pulse`, `main` branch)
- **Domain:** `pulse.krv.co` (CNAME → `MCRabonza.github.io`)
- **DNS:** GoDaddy (`krv.co` registrar)
- **Fonts:** Adobe Typekit Kit `lso5kkg` (`miller-display`, `articulat-cf`, `shippori-antique`)
- **Charts:** Chart.js 4.4.0 + chartjs-plugin-annotation 2.2.1

---

## Brand

- Primary Green: `#142D23`
- Secondary / Cream: `#F7F3E7`
- Highlight: `#E7F0EB`
- Accent: `#4A8F7E`
- Fonts: `miller-display` (italic headings) · `articulat-cf` (body/labels)

---

**KRV & Co. Internal · mcr@krv.co · www.krv.co**
