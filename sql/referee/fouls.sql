-- 4) Referees who have shown a red card
SELECT
    r.name AS referee,
    r.country,
    m.match_id,
    m.date,
    ht.fifa_code || ' VS ' || at.fifa_code AS match,
    t.fifa_code AS carded_team,
    ps.player_name,
    me.minute
FROM match_events AS me
JOIN matches AS m
    ON me.match_id = m.match_id
JOIN referees AS r
    ON m.referee_id = r.referee_id
JOIN teams AS t
    ON me.team_id = t.team_id
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
JOIN player_stats AS ps
    ON me.player_id = ps.player_id
WHERE me.event_type = 'Red Card'
ORDER BY m.date ASC;