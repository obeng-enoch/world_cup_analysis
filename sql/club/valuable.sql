-- 3) Most valuable clubs by combined market value of players sent
SELECT
    sp.club_team,
    COUNT(*) AS players_sent,
    ROUND(SUM(sp.market_value_eur), 2) AS total_market_value_eur,
    ROUND(AVG(sp.market_value_eur), 2) AS avg_market_value_eur
FROM squads_and_players AS sp
GROUP BY sp.club_team
ORDER BY total_market_value_eur DESC
LIMIT 10;
