# Executive KPI & Wealth Management Analytics

End-to-end portfolio project simulating a management reporting workflow for a wealth-management-style business using **synthetic data**.

## Business objective
Turn monthly operating data into reliable management information: calculate NNA, validate KPI inputs, compare actuals with targets, benchmark business units, identify flow and retention trends, and produce concise management actions.

## Analytics workflow
1. **SQL** — aggregation, KPI calculations, data-quality checks, target variance and business-unit benchmarking.
2. **Python / Pandas** — transformation, derived metrics, trend analysis and management commentary.
3. **Power BI** — executive dashboard design with DAX measures and reconciliation against SQL/Python outputs.

## Key KPIs
- Assets under management (AUM)
- Inflows and outflows
- Net New Assets (NNA)
- NNA target attainment and variance
- Net flow rate
- Revenue and operating margin
- Client retention
- Business-unit performance
- Month-over-month NNA movement

## Management use cases
- Daily/weekly/monthly management reporting patterns
- KPI trend and exception analysis
- Actual-vs-target comparison
- Business-unit benchmarking
- Data validation and reconciliation
- Flow-driver investigation
- Executive-ready commentary

## Technology
**SQL | Python | Pandas | Power BI | DAX | CSV | Git/GitHub**

## Repository structure
```text
Executive_KPI_Reporting/
├── README.md
├── requirements.txt
├── data/
│   ├── monthly_kpis.csv
│   └── DATA_DICTIONARY.md
├── sql/
│   ├── executive_kpi_queries.sql
│   └── validation_and_insights.sql
├── src/
│   ├── executive_kpi.py
│   └── insights.py
└── powerbi/
    ├── README.md
    └── dax_measures.dax
```

## Run locally
```bash
pip install -r requirements.txt
python src/executive_kpi.py
python src/insights.py
```

## Power BI
Load `data/monthly_kpis.csv`, create the measures in `powerbi/dax_measures.dax`, and build executive, business-unit, and flow/retention views. Validate Power BI totals against the SQL and Python outputs.

## Portfolio disclaimer
All data is synthetic. This is an independent portfolio project and is **not Morgan Stanley data, systems, or employment experience**.