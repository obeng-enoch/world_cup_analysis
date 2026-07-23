-- Most saves (goalkeepers)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.position,
    ps.saves,
    ps.clean_sheets,
    ps.goals_conceded,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.position = 'GK' AND ps.saves > 0
ORDER BY ps.saves DESC, ps.clean_sheets DESC, ps.minutes_played DESC
LIMIT 10;