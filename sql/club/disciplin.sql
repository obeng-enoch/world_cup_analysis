-- 8) Discipline record by club
SELECT
    sp.club_team,
    COUNT(DISTINCT sp.player_id) AS players_sent,
    SUM(ps.yellow_cards) AS total_yellow_cards,
    SUM(ps.red_cards) AS total_red_cards
FROM squads_and_players AS sp
JOIN player_stats AS ps
    ON sp.player_id = ps.player_id
GROUP BY sp.club_team
HAVING SUM(ps.yellow_cards + ps.red_cards) > 0
ORDER BY total_red_cards DESC, total_yellow_cards DESC
LIMIT 10;