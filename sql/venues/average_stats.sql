-- 8) Average possession, corners, fouls, offsides per venue
SELECT
    v.stadium_name,
    COUNT(DISTINCT m.match_id) AS matches_played,
    ROUND(AVG(mts.possession_pct), 2) AS avg_possession_pct,
    ROUND(AVG(mts.corners), 2) AS avg_corners,
    ROUND(AVG(mts.fouls), 2) AS avg_fouls,
    ROUND(AVG(mts.offsides), 2) AS avg_offsides
FROM match_team_stats AS mts
JOIN matches AS m
    ON mts.match_id = m.match_id
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY v.venue_id, v.stadium_name
ORDER BY avg_fouls DESC
LIMIT 10;