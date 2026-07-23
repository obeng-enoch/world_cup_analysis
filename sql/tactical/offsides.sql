-- 11) Offside frequency per team (high-line/attacking-pace proxy)
SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    SUM(mts.offsides) AS total_offsides,
    ROUND(AVG(mts.offsides), 2) AS avg_offsides_per_match
FROM match_team_stats AS mts
JOIN teams AS t
    ON mts.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY avg_offsides_per_match DESC
LIMIT 10;