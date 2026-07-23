-- 5) Average possession, corners, fouls, offsides per team
SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    ROUND(AVG(mts.possession_pct), 2) AS avg_possession_pct,
    ROUND(AVG(mts.corners), 2) AS avg_corners,
    ROUND(AVG(mts.fouls), 2) AS avg_fouls,
    ROUND(AVG(mts.offsides), 2) AS avg_offsides
FROM match_team_stats AS mts
JOIN matches AS m
    ON mts.match_id = m.match_id
JOIN teams AS t
    ON mts.team_id = t.team_id
WHERE m.status = 'Completed'
GROUP BY t.fifa_code
ORDER BY avg_possession_pct DESC;