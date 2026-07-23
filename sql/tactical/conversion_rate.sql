-- 4) Shooting efficiency per team (shots vs shots on target vs goals)
WITH team_matches AS (
    SELECT m.match_id, m.home_team_id AS team_id, m.home_score AS goals_for
    FROM matches AS m
    WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.match_id, m.away_team_id AS team_id, m.away_score AS goals_for
    FROM matches AS m
    WHERE m.status = 'Completed'
)
SELECT
    t.fifa_code AS team,
    SUM(mts.total_shots) AS total_shots,
    SUM(mts.shots_on_target) AS shots_on_target,
    SUM(tm.goals_for) AS goals_for,
    ROUND(SUM(mts.shots_on_target) * 100.0 / NULLIF(SUM(mts.total_shots), 0), 2) AS shot_accuracy_pct,
    ROUND(SUM(tm.goals_for) * 100.0 / NULLIF(SUM(mts.shots_on_target), 0), 2) AS conversion_of_shots_on_target_pct
FROM match_team_stats AS mts
JOIN team_matches AS tm
    ON mts.match_id = tm.match_id AND mts.team_id = tm.team_id
JOIN teams AS t
    ON mts.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY shot_accuracy_pct DESC
LIMIT 10;