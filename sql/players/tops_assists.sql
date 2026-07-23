-- Top assist providers
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.assists,
    ps.goals,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.assists > 0
ORDER BY ps.assists DESC, ps.goals DESC, ps.minutes_played ASC
LIMIT 10;