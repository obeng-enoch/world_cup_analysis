-- Own goals
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.own_goals,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.own_goals > 0
ORDER BY ps.own_goals DESC, ps.matches_played DESC
LIMIT 10;