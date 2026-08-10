-- 2) Matches hosted per country/city
SELECT
    v.country,
    v.city,
    COUNT(m.match_id) AS matches_hosted
FROM venues AS v
JOIN matches AS m
    ON v.venue_id = m.venue_id
WHERE m.status = 'Completed'
GROUP BY v.country, v.city
ORDER BY matches_hosted DESC;