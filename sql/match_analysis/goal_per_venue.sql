-- 9) Matches and goals per venue
SELECT
    v.stadium_name,
    v.city,
    v.country,
    v.capacity,
    COUNT(*) AS matches_hosted,
    SUM(m.home_score + m.away_score) AS total_goals,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY v.venue_id, v.stadium_name, v.city, v.country, v.capacity
ORDER BY matches_hosted DESC, avg_goals_per_match DESC;