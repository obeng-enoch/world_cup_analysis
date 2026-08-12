-- 8) Matches officiated per referee by stage (trust in high-stakes games)
SELECT
    r.name AS referee,
    ts.stage_name AS stage,
    COUNT(*) AS matches_officiated
FROM matches AS m
JOIN referees AS r
    ON m.referee_id = r.referee_id
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
GROUP BY r.referee_id, r.name, ts.stage_name, ts.is_knockout
ORDER BY r.name ASC, matches_officiated DESC;