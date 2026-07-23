-- Goal contributions (goals + assists)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    (ps.goals + ps.assists) AS goal_contributions,
    ps.goals,
    ps.assists,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE (ps.goals + ps.assists) > 0
ORDER BY goal_contributions DESC, ps.goals DESC, ps.assists DESC
LIMIT 10;