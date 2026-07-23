-- 7) Squad market value
SELECT
    t.fifa_code AS team,
    COUNT(*) AS squad_size,
    ROUND(SUM(sp.market_value_eur), 2) AS total_market_value_eur,
    ROUND(AVG(sp.market_value_eur), 2) AS avg_market_value_eur
FROM squads_and_players AS sp
JOIN teams AS t
    ON sp.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY total_market_value_eur DESC;