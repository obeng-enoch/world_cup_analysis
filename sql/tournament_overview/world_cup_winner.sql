-- 0) Tournament Finish Summary — each team's furthest stage reached
-- and how their tournament ultimately ended
WITH team_matches AS (
    SELECT
        m.match_id,
        m.stage_id,
        m.home_team_id AS team_id,
        m.home_score AS goals_for,
        m.away_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'

    UNION ALL

    SELECT
        m.match_id,
        m.stage_id,
        m.away_team_id AS team_id,
        m.away_score AS goals_for,
        m.home_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
),

furthest_stage AS (
    SELECT
        team_id,
        MAX(stage_id) AS max_stage_id
    FROM team_matches
    GROUP BY team_id
),

final_match AS (
    SELECT
        tm.team_id,
        tm.stage_id,
        CASE
            WHEN tm.goals_for > tm.goals_against THEN 'Win'
            WHEN tm.goals_for < tm.goals_against THEN 'Loss'
            ELSE 'Draw'
        END AS result,
        ROW_NUMBER() OVER (PARTITION BY tm.team_id ORDER BY tm.match_id) AS rn
    FROM team_matches AS tm
    JOIN furthest_stage AS fs
        ON tm.team_id = fs.team_id
        AND tm.stage_id = fs.max_stage_id
)

SELECT
    t.team_name
FROM final_match AS fm
JOIN teams AS t
    ON fm.team_id = t.team_id
WHERE
    fm.rn = 1
    AND fm.stage_id = 7
    AND fm.result = 'Win';