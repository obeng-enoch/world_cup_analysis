-- 3) Possession style tiers and results within each tier
WITH team_matches AS (
    SELECT m.match_id, m.home_team_id AS team_id,
           m.home_score AS goals_for, m.away_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.match_id, m.away_team_id AS team_id,
           m.away_score AS goals_for, m.home_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
)
SELECT
    CASE
        WHEN mts.possession_pct >= 60 THEN 'High possession (60%+)'
        WHEN mts.possession_pct >= 45 THEN 'Balanced (45-60%)'
        ELSE 'Low possession (<45%)'
    END AS possession_tier,
    COUNT(*) AS matches,
    SUM(CASE WHEN tm.goals_for > tm.goals_against THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN tm.goals_for = tm.goals_against THEN 1 ELSE 0 END) AS draws,
    SUM(CASE WHEN tm.goals_for < tm.goals_against THEN 1 ELSE 0 END) AS losses,
    ROUND(AVG(tm.goals_for), 2) AS avg_goals_for
FROM match_team_stats AS mts
JOIN team_matches AS tm
    ON mts.match_id = tm.match_id AND mts.team_id = tm.team_id
GROUP BY possession_tier
ORDER BY AVG(mts.possession_pct) DESC;