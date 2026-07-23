-- Most starts
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.matches_started,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.matches_started > 0
ORDER BY ps.matches_started DESC, ps.minutes_played DESC
LIMIT 10;