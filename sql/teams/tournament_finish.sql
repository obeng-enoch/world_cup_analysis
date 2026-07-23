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
    t.fifa_code AS team,
    t.confederation,
    ts.stage_name AS stage_reached,
    CASE
        WHEN fm.stage_id = 7 AND fm.result = 'Win'             THEN 'Champion'
        WHEN fm.stage_id = 7 AND fm.result IN ('Loss','Draw')  THEN 'Runner-up'
        WHEN fm.stage_id = 6 AND fm.result = 'Win'             THEN 'Third Place'
        WHEN fm.stage_id = 6 AND fm.result IN ('Loss','Draw')  THEN 'Fourth Place'
        WHEN fm.stage_id = 5                                   THEN 'Semi-finalist'
        WHEN fm.stage_id = 4                                   THEN 'Quarter-finalist'
        WHEN fm.stage_id = 3                                   THEN 'Round of 16'
        WHEN fm.stage_id = 2                                   THEN 'Round of 32'
        WHEN fm.stage_id = 1                                   THEN 'Eliminated - Group Stage'
        ELSE 'Unknown'
    END AS tournament_finish,
    CASE
        WHEN fm.stage_id = 7 AND fm.result = 'Win'             THEN 1
        WHEN fm.stage_id = 7 AND fm.result IN ('Loss','Draw')  THEN 2
        WHEN fm.stage_id = 6 AND fm.result = 'Win'             THEN 3
        WHEN fm.stage_id = 6 AND fm.result IN ('Loss','Draw')  THEN 4
        WHEN fm.stage_id = 5                                   THEN 5
        WHEN fm.stage_id = 4                                   THEN 6
        WHEN fm.stage_id = 3                                   THEN 7
        WHEN fm.stage_id = 2                                   THEN 8
        WHEN fm.stage_id = 1                                   THEN 9
        ELSE 10
    END AS finish_rank
FROM final_match AS fm
JOIN teams AS t ON fm.team_id = t.team_id
JOIN tournament_stages AS ts ON fm.stage_id = ts.stage_id
WHERE fm.rn = 1
ORDER BY finish_rank;