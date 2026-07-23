WITH team_matches AS ( /* same as above */
    SELECT m.match_id, m.stage_id, m.home_team_id AS team_id,
           m.home_score AS goals_for, m.away_score AS goals_against
    FROM matches AS m WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.match_id, m.stage_id, m.away_team_id AS team_id,
           m.away_score AS goals_for, m.home_score AS goals_against
    FROM matches AS m WHERE m.status = 'Completed'
),
furthest_stage AS (
    SELECT team_id, MAX(stage_id) AS max_stage_id
    FROM team_matches GROUP BY team_id
),
final_match AS (
    SELECT tm.team_id, tm.stage_id,
        CASE
            WHEN tm.goals_for > tm.goals_against THEN 'Win'
            WHEN tm.goals_for < tm.goals_against THEN 'Loss'
            ELSE 'Draw'
        END AS result,
        ROW_NUMBER() OVER (PARTITION BY tm.team_id ORDER BY tm.match_id) AS rn
    FROM team_matches AS tm
    JOIN furthest_stage AS fs
        ON tm.team_id = fs.team_id AND tm.stage_id = fs.max_stage_id
),
team_finish AS (
    SELECT fm.team_id,
        CASE
            WHEN fm.stage_id = 7 AND fm.result = 'Win'             THEN 'Champion'
            WHEN fm.stage_id = 7 AND fm.result IN ('Loss','Draw')  THEN 'Runner-up'
            WHEN fm.stage_id = 6 AND fm.result = 'Win'             THEN 'Third Place'
            WHEN fm.stage_id = 6 AND fm.result IN ('Loss','Draw')  THEN 'Fourth Place'
            ELSE 'Other'
        END AS tournament_finish
    FROM final_match AS fm
    WHERE fm.rn = 1
)

SELECT
    sp.club_team,
    SUM(CASE WHEN tf.tournament_finish = 'Champion'    THEN 1 ELSE 0 END) AS gold,
    SUM(CASE WHEN tf.tournament_finish = 'Runner-up'   THEN 1 ELSE 0 END) AS silver,
    SUM(CASE WHEN tf.tournament_finish = 'Third Place' THEN 1 ELSE 0 END) AS bronze,
    SUM(CASE WHEN tf.tournament_finish IN ('Champion','Runner-up','Third Place') THEN 1 ELSE 0 END) AS total_medals
FROM squads_and_players AS sp
JOIN team_finish AS tf
    ON sp.team_id = tf.team_id
GROUP BY sp.club_team
HAVING total_medals > 0
ORDER BY total_medals DESC, gold DESC, silver DESC, bronze DESC;