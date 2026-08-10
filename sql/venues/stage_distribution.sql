-- 5) Stage distribution per venue (group stage vs knockout load)
SELECT
    v.stadium_name,
    ts.stage_name AS stage,
    COUNT(*) AS matches_hosted
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
GROUP BY v.stadium_name, ts.stage_name
ORDER BY v.stadium_name ASC, matches_hosted DESC;