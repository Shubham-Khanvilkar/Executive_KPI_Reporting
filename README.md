# Executive KPI Reporting

Independent portfolio project simulating a management reporting pack for a financial-services-style operating environment using synthetic data.

## Objective
Transform monthly operating data into executive KPIs, trend analysis, variance analysis, and management-ready commentary.

## KPIs
- Assets under management (AUM)
- Net New Assets (NNA)
- Net flow rate
- Revenue
- Operating expense
- Operating margin
- Client retention
- Advisor productivity
- Month-over-month movement

## Analysis
The reporting layer identifies KPI movements, compares actuals with targets, ranks business units, and produces concise exception commentary for management review.

## Technology
Python, Pandas, SQL, CSV, Git/GitHub

## Run locally
```bash
pip install -r requirements.txt
python src/executive_kpi.py
```

## Structure
```text
Executive_KPI_Reporting/
├── README.md
├── .gitattributes
├── requirements.txt
├── data/
│   └── monthly_kpis.csv
├── src/
│   └── executive_kpi.py
└── sql/
    └── executive_kpi_queries.sql
```

## Portfolio disclaimer
All data is synthetic. This is an independent portfolio project and is not professional Morgan Stanley or financial-services employment experience.
