-- ==========================================================
-- 3) Highest Scoring Matches
-- ==========================================================

SELECT

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    ts.stage_name AS stage,

    CAST(m.home_score+m.away_score AS INTEGER) AS total_goals

FROM matches m

JOIN teams ht
ON m.home_team_id=ht.team_id

JOIN teams at
ON m.away_team_id=at.team_id

JOIN tournament_stages ts
ON m.stage_id=ts.stage_id

WHERE m.status='Completed'

ORDER BY total_goals DESC

LIMIT 10;