-- 2) Average events per match by type
WITH match_count AS (
    SELECT COUNT(*) AS total_matches
    FROM matches
    WHERE status = 'Completed'
)
SELECT
    me.event_type,
    COUNT(*) AS total_events,
    ROUND(COUNT(*) * 1.0 / (SELECT total_matches FROM match_count), 2) AS avg_events_per_match
FROM match_events AS me
JOIN matches AS m
    ON me.match_id = m.match_id
WHERE m.status = 'Completed'
GROUP BY me.event_type
ORDER BY avg_events_per_match DESC;