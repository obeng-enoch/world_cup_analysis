-- 7) Late goals (85th minute or later)
SELECT

        ps.player_name,

    t.fifa_code,

    me.minute || '''' AS minute,

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code
    AS match,

    DATE(m.date) AS match_date,

    ts.stage_name

FROM match_events AS me
JOIN matches AS m
    ON me.match_id = m.match_id
JOIN teams AS t
    ON me.team_id = t.team_id
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
JOIN player_stats AS ps
    ON me.player_id = ps.player_id
WHERE me.event_type = 'Goal' AND me.minute >= 85
ORDER BY me.minute DESC;