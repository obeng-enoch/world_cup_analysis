-- KPI 5: Total Goals
SELECT
    SUM(home_score + away_score) AS total_goals
FROM matches
WHERE status = 'Completed';