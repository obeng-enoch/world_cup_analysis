-- 3) Matches, goals, and average goals per venue
SELECT
    v.stadium_name,
    v.city,
    v.country,
    COUNT(*) AS matches_hosted,
    SUM(m.home_score + m.away_score) AS total_goals,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY v.venue_id, v.stadium_name, v.city, v.country
ORDER BY avg_goals_per_match DESC, matches_hosted DESC
LIMIT 10;