-- ==========================================================
-- 3) Most Aggressive Attacking Teams
-- ==========================================================
SELECT
    t.fifa_code AS team,

    COUNT(*) AS matches_played,

    SUM(mts.total_shots) AS total_shots,

    SUM(mts.shots_on_target) AS shots_on_target,

    ROUND(AVG(mts.total_shots),2) AS shots_per_match,

    ROUND(AVG(mts.shots_on_target),2) AS shots_on_target_per_match

FROM match_team_stats mts

JOIN matches m
ON mts.match_id=m.match_id

JOIN teams t
ON mts.team_id=t.team_id

WHERE m.status='Completed'

GROUP BY t.fifa_code

ORDER BY
total_shots DESC,
shots_on_target DESC;