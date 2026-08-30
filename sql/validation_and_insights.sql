-- Data-quality checks
SELECT COUNT(*) AS row_count,
       COUNT(DISTINCT month) AS reporting_months,
       COUNT(DISTINCT business_unit) AS business_units
FROM monthly_kpis;

-- Missing-value check
SELECT
    SUM(CASE WHEN aum IS NULL THEN 1 ELSE 0 END) AS missing_aum,
    SUM(CASE WHEN inflows IS NULL THEN 1 ELSE 0 END) AS missing_inflows,
    SUM(CASE WHEN outflows IS NULL THEN 1 ELSE 0 END) AS missing_outflows,
    SUM(CASE WHEN target_nna IS NULL THEN 1 ELSE 0 END) AS missing_targets
FROM monthly_kpis;

-- NNA and target variance
SELECT
    month,
    business_unit,
    inflows,
    outflows,
    inflows - outflows AS nna,
    target_nna,
    (inflows - outflows) - target_nna AS nna_variance,
    CASE
        WHEN target_nna = 0 THEN NULL
        ELSE (inflows - outflows) / target_nna
    END AS nna_attainment
FROM monthly_kpis
ORDER BY month, business_unit;

-- Business-unit benchmarking
SELECT
    business_unit,
    SUM(aum) AS total_aum,
    SUM(inflows - outflows) AS total_nna,
    SUM(revenue) AS total_revenue,
    SUM(opex) AS total_opex,
    SUM(retained_clients) * 1.0 / NULLIF(SUM(clients),0) AS retention_rate
FROM monthly_kpis
GROUP BY business_unit
ORDER BY total_nna DESC;

-- Flow-driver investigation
SELECT
    month,
    SUM(inflows) AS total_inflows,
    SUM(outflows) AS total_outflows,
    SUM(inflows - outflows) AS nna
FROM monthly_kpis
GROUP BY month
ORDER BY month;