-- Most minutes played
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.minutes_played,
    ps.matches_played,
    ps.matches_started
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.minutes_played > 0
ORDER BY ps.minutes_played DESC, ps.matches_played DESC
LIMIT 10;