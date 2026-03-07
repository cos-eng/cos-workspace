# ORG_CHART.md — Organization Structure

## Last Updated: 2026-03-06

## Company: Tatvic Analytics

| Sr. No | Team | Team Lead | Reports To | North Star KPI |
|--------|------|-----------|-----------|---------------|
| 1 | Account Management | Rikita Shukla | Sarjal Patel | Total Net PO value from Existing Customers ≥ INR 10 CR |
| 2 | Account Management | Neha Singh | Sarjal Patel | _(shared KPI with Rikita)_ |
| 3 | Accounts & Finance | Chandni Sedani | Ravi Pathak | Internal Audits completed per quarter ≥ 4; Post-due compliance ≤ 3/year |
| 4 | Customer Development | Maulin Joshi | Khilav Joshi | Net PO Value from New Client Onboarding ≥ INR 15 CR (CY 2026) |
| 5 | HR | Dhwani Shah | Khilav Joshi | Days to offer acceptance for open positions ≤ 45 days |
| 6 | IT & Admin | Devang Pathak | Rajiv Pathak | Aggregate Leader/HOD satisfaction score ≥ 4.5 |
| 7 | Legal | Chandni Sedani | Ravi Pathak | Commercial agreement turnaround ≤ 36 working hours (excl. NDA) |
| 8 | Marketing | Ankita Singh | Khilav Joshi | MQLs generated in CY 2026; PO value from MQL leads ≥ INR 10 CR |
| 9 | Solution Architect | Lakshin Pathak | Khilav Joshi | Agentic AI Projects/Experiments completed ≥ 3 |
| 10 | Customer Delivery | Sarjak Patel | Khilav Joshi | Workflows with Agentic AI component ≥ 80% |
| 20 | Customer Delivery | Kamal Aggarwal | Sarjak Patel | _(rollup from sub-teams)_ |
| 21 | Customer Delivery — Campaign Management | Bhumita Sarabhai | Kamal Aggarwal | — |
| 11 | Customer Delivery — CRO | Kshitija Bakre | Kamal Aggarwal | — |
| 19 | Customer Delivery | Prakash Katariya | Kamal Aggarwal | _(rollup from sub-teams)_ |
| 12 | Customer Delivery — Data Collection (QA) | Ekta Joshi | Prakash Katariya | — |
| 13 | Customer Delivery — Data Collection | Maulik Patel | Prakash Katariya | — |
| 14 | Customer Delivery — Data Analysis & Insight | Harsh Panchal | Prakash Katariya | — |
| 15 | Customer Delivery — Data Collection | Kalpit Visavadiya | Prakash Katariya | — |
| 16 | Customer Delivery — Data Analysis & Insight | Ashlesha Choudhari | Prakash Katariya | — |
| 17 | Customer Delivery — Data Engineer | Jeet Shah | Kamal Aggarwal | — |
| 18 | Customer Delivery — Data Science | Rushabh Shah | Kamal Aggarwal | — |

## Reporting Hierarchy

```text
CEO (Khilav Joshi)
├── Customer Development (Lead: Maulin Joshi)
├── HR (Lead: Dhwani Shah)
├── Marketing (Lead: Ankita Singh)
├── Solution Architect (Lead: Lakshin Pathak)
├── Customer Delivery (Lead: Sarjak Patel)
│   ├── Customer Delivery (Lead: Kamal Aggarwal)
│   │   ├── Campaign Management (Lead: Bhumita Sarabhai)
│   │   ├── CRO (Lead: Kshitija Bakre)
│   │   ├── Data Engineer (Lead: Jeet Shah)
│   │   ├── Data Science (Lead: Rushabh Shah)
│   │   └── Customer Delivery (Lead: Prakash Katariya)
│   │       ├── Data Collection QA (Lead: Ekta Joshi)
│   │       ├── Data Collection (Lead: Maulik Patel)
│   │       ├── Data Analysis & Insight (Lead: Harsh Panchal)
│   │       ├── Data Collection (Lead: Kalpit Visavadiya)
│   │       └── Data Analysis & Insight (Lead: Ashlesha Choudhari)
│   └── Account Management (Lead: Sarjal Patel)  ← reports via Sarjak
│       ├── Rikita Shukla
│       └── Neha Singh
├── Accounts & Finance (Lead: Chandni Sedani → Ravi Pathak)
├── IT & Admin (Lead: Devang Pathak → Rajiv Pathak)
└── Legal (Lead: Chandni Sedani → Ravi Pathak)
```

## Strategic Objective Mapping

| Team | Likely SO Link | Rationale |
|------|---------------|-----------|
| Account Management | SO-1 (Revenue) | Net PO value from existing customers |
| Customer Development | SO-1 (Revenue) | New client onboarding PO value |
| Marketing | SO-1 (Revenue) | MQL generation → PO conversions |
| Customer Delivery | SO-2 (Agentic AI) | 80% workflows with Agentic AI component |
| Solution Architect | SO-2 (Agentic AI) | Agentic AI projects/experiments |
| HR | SO-3 (Ops) | Hiring speed optimization |
| IT & Admin | SO-3 (Ops) | Internal service quality |
| Accounts & Finance | SO-3 (Ops) | Audit and compliance |
| Legal | SO-3 (Ops) | Commercial agreement turnaround |

> **Note:** SO links are inferred. CEO Khilav should validate these against SOUL.md objectives.

## Update Rules

- Update when team structure changes (new hires, departures, reorgs)
- Each team must be linked to a Strategic Objective from SOUL.md
- North Star KPI must be measurable and tracked in Daily Briefing §3
- Source: [Org Structure_Mar 26.md](Org%20Structure_Mar%2026.md)
