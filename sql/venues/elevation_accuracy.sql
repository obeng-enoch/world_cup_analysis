-- 6) Goals and xG accuracy by elevation band
SELECT
    CASE
        WHEN v.elevation_meters < 500 THEN 'Low (<500m)'
        WHEN v.elevation_meters < 1500 THEN 'Mid (500-1500m)'
        ELSE 'High (1500m+)'
    END AS elevation_band,
    COUNT(*) AS matches_played,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match,
    ROUND(AVG(m.home_xg + m.away_xg), 2) AS avg_combined_xg
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY elevation_band
ORDER BY AVG(v.elevation_meters) ASC;