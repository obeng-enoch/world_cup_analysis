-- 7) Minutes played contributed by club (squad game-time footprint)
SELECT
    sp.club_team,
    COUNT(DISTINCT sp.player_id) AS players_sent,
    SUM(ps.minutes_played) AS total_minutes_played,
    ROUND(AVG(ps.minutes_played), 2) AS avg_minutes_per_player
FROM squads_and_players AS sp
JOIN player_stats AS ps
    ON sp.player_id = ps.player_id
GROUP BY sp.club_team
ORDER BY total_minutes_played DESC
LIMIT 10;