-- Multi-goal matches (2+ goals)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ht.fifa_code || ' ' || CAST(m.home_score AS INTEGER) || '–' || CAST(m.away_score AS INTEGER) || ' ' || at.fifa_code AS match,
    ts.stage_name AS stage,
    COUNT(*) AS goals
FROM match_events AS me
JOIN player_stats AS ps ON me.player_id = ps.player_id
JOIN teams AS t ON ps.team_id = t.team_id
JOIN matches AS m ON me.match_id = m.match_id
JOIN teams AS ht ON m.home_team_id = ht.team_id
JOIN teams AS at ON m.away_team_id = at.team_id
JOIN tournament_stages AS ts ON m.stage_id = ts.stage_id
WHERE me.event_type = 'Goal'
GROUP BY me.match_id, ps.player_id, ps.player_name, t.fifa_code, ht.fifa_code, at.fifa_code
HAVING COUNT(*) >= 2
ORDER BY goals DESC, ps.player_name;