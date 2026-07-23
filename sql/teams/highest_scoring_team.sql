-- 1) Highest Scoring Teams
-- ==========================================================
WITH team_attack AS (
    SELECT
        m.match_id,
        m.home_team_id AS team_id,
        m.home_score AS goals_for
    FROM matches AS m
    WHERE m.status = 'Completed'

    UNION ALL

    SELECT
        m.match_id,
        m.away_team_id,
        m.away_score
    FROM matches AS m
    WHERE m.status = 'Completed'
)

SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    SUM(ta.goals_for) AS goals,
    ROUND(AVG(ta.goals_for),2) AS goals_per_match,

    SUM(mts.total_shots) AS shots,
    SUM(mts.shots_on_target) AS shots_on_target,

    ROUND(
        CASE
            WHEN SUM(mts.total_shots) > 0
            THEN SUM(ta.goals_for) * 100.0 / SUM(mts.total_shots)
        END,
    2) AS shot_conversion_pct

FROM team_attack ta

JOIN match_team_stats mts
ON ta.match_id = mts.match_id
AND ta.team_id = mts.team_id

JOIN teams t
ON ta.team_id = t.team_id

GROUP BY t.fifa_code

ORDER BY
goals DESC,
goals_per_match DESC;