-- 2) Referees by country
SELECT
    r.country,
    COUNT(DISTINCT r.referee_id) AS referees_assigned,
    COUNT(m.match_id) AS matches_officiated
FROM referees AS r
LEFT JOIN matches AS m
    ON r.referee_id = m.referee_id AND m.status = 'Completed'
GROUP BY r.country
ORDER BY matches_officiated DESC