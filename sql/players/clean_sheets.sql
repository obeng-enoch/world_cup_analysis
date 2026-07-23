-- Most clean sheets (goalkeepers)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.position,
    ps.clean_sheets,
    ps.goals_conceded,
    ps.saves,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.position = 'GK' AND ps.clean_sheets > 0
ORDER BY ps.clean_sheets DESC, ps.matches_played DESC, ps.minutes_played DESC
LIMIT 10;