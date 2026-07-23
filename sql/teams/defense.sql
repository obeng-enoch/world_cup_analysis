-- ==========================================================
-- SECTION C — DEFENSE
-- ==========================================================

-- 4) Best defensive teams (goals conceded, clean sheets)
WITH team_matches AS (
    SELECT m.home_team_id AS team_id, m.away_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.away_team_id AS team_id, m.home_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
)
SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    SUM(tm.goals_against) AS goals_against,
    ROUND(AVG(tm.goals_against), 2) AS goals_conceded_per_match,
    SUM(CASE WHEN tm.goals_against = 0 THEN 1 ELSE 0 END) AS clean_sheets
FROM team_matches AS tm
JOIN teams AS t
    ON tm.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY goals_conceded_per_match ASC, clean_sheets DESC
LIMIT 10;