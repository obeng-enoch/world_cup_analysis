-- Penalty goals
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.penalty_goals,
    ps.goals
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.penalty_goals > 0
ORDER BY ps.penalty_goals DESC
LIMIT 10;