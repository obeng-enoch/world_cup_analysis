-- 11) Matches and goals per stage
SELECT
    ts.stage_name AS stage,
    COUNT(*) AS matches_played,
    SUM(m.home_score + m.away_score) AS total_goals,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match
FROM matches AS m
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
WHERE m.status = 'Completed'
GROUP BY ts.stage_id, ts.stage_name, ts.is_knockout
ORDER BY ts.stage_id ASC;