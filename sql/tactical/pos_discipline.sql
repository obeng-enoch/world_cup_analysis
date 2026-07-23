-- 9) Discipline by position
SELECT
    ps.position,
    COUNT(DISTINCT ps.player_id) AS players,
    SUM(ps.yellow_cards) AS yellow_cards,
    SUM(ps.red_cards) AS red_cards,
    ROUND((SUM(ps.yellow_cards + ps.red_cards) * 1.0) / NULLIF(COUNT(DISTINCT ps.player_id), 0), 2) AS cards_per_player
FROM player_stats AS ps
GROUP BY ps.position
ORDER BY cards_per_player DESC;