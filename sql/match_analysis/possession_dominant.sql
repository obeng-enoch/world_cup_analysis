-- 13) Most/least possession-dominant matches
SELECT
    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    ht.fifa_code
    || ' '
    || CAST(home_stats.possession_pct AS INTEGER)
    || '–'
    || CAST(away_stats.possession_pct AS INTEGER)
    || ' '
    || at.fifa_code AS possession,

    ABS(home_stats.possession_pct - away_stats.possession_pct) AS possession_gap

FROM matches AS m
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
JOIN match_team_stats AS home_stats
    ON home_stats.match_id = m.match_id AND home_stats.team_id = m.home_team_id
JOIN match_team_stats AS away_stats
    ON away_stats.match_id = m.match_id AND away_stats.team_id = m.away_team_id
WHERE m.status = 'Completed'
ORDER BY possession_gap DESC
LIMIT 10;