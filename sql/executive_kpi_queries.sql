-- Monthly executive KPI summary
SELECT
    month,
    SUM(aum) AS total_aum,
    SUM(inflows) AS inflows,
    SUM(outflows) AS outflows,
    SUM(inflows - outflows) AS nna,
    SUM(revenue) AS revenue,
    SUM(opex) AS opex,
    SUM(revenue - opex) AS operating_profit,
    ROUND(SUM(revenue - opex) / NULLIF(SUM(revenue), 0), 4) AS operating_margin,
    ROUND(SUM(inflows - outflows) / NULLIF(SUM(aum), 0), 4) AS net_flow_rate
FROM monthly_kpis
GROUP BY month
ORDER BY month;

-- Business-unit ranking
SELECT
    business_unit,
    SUM(aum) AS aum,
    SUM(inflows - outflows) AS nna,
    SUM(revenue) AS revenue,
    SUM(opex) AS opex,
    ROUND(SUM(revenue - opex) / NULLIF(SUM(revenue), 0), 4) AS operating_margin
FROM monthly_kpis
GROUP BY business_unit
ORDER BY nna DESC;

-- Target attainment by month
SELECT
    month,
    SUM(inflows - outflows) AS actual_nna,
    SUM(target_nna) AS target_nna,
    ROUND(SUM(inflows - outflows) / NULLIF(SUM(target_nna), 0), 4) AS nna_attainment
FROM monthly_kpis
GROUP BY month
ORDER BY month;

-- Retention KPI
SELECT
    month,
    SUM(retained_clients) AS retained_clients,
    SUM(clients) AS clients,
    ROUND(SUM(retained_clients) / NULLIF(SUM(clients), 0), 4) AS retention_rate
FROM monthly_kpis
GROUP BY month
ORDER BY month;
