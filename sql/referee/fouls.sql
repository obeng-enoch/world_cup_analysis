SELECT
    r.name AS referee,
    r.country,
    COUNT(DISTINCT m.match_id) AS matches_officiated,
    ROUND(AVG(match_fouls.total_fouls), 2) AS avg_fouls_per_match
FROM matches AS m
JOIN referees AS r
    ON m.referee_id = r.referee_id
JOIN (
    SELECT match_id, SUM(fouls) AS total_fouls
    FROM match_team_stats
    GROUP BY match_id
) AS match_fouls
    ON match_fouls.match_id = m.match_id
WHERE m.status = 'Completed'
GROUP BY r.referee_id, r.name, r.country
ORDER BY avg_fouls_per_match DESC
LIMIT 10;