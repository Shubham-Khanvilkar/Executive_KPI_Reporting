-- Power BI source query: monthly business-unit fact set
SELECT
    CAST(month AS DATE) AS month,
    business_unit,
    aum,
    inflows,
    outflows,
    inflows - outflows AS nna,
    revenue,
    opex,
    revenue - opex AS operating_profit,
    clients,
    retained_clients,
    advisors,
    target_nna,
    (inflows - outflows) - target_nna AS nna_variance
FROM monthly_kpis
ORDER BY month, business_unit;

-- Power BI validation: monthly totals
SELECT
    CAST(month AS DATE) AS month,
    SUM(aum) AS total_aum,
    SUM(inflows) AS total_inflows,
    SUM(outflows) AS total_outflows,
    SUM(inflows - outflows) AS total_nna,
    SUM(target_nna) AS total_target_nna
FROM monthly_kpis
GROUP BY CAST(month AS DATE)
ORDER BY month;

-- Power BI validation: business-unit totals
SELECT
    business_unit,
    SUM(aum) AS total_aum,
    SUM(inflows - outflows) AS total_nna,
    SUM(revenue) AS total_revenue,
    SUM(revenue - opex) AS operating_profit
FROM monthly_kpis
GROUP BY business_unit
ORDER BY total_nna DESC;
