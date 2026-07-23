-- Lowest goals conceded (min 180 minutes)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.position,
    ps.goals_conceded,
    ps.minutes_played,
    ps.clean_sheets,
    ps.saves
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.position = 'GK' AND ps.minutes_played >= 180
ORDER BY ps.goals_conceded ASC, ps.minutes_played DESC
LIMIT 10;