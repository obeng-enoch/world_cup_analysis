-- ==========================================================
-- 1) Full Match Schedule   
-- ==========================================================
SELECT
    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,
    DATE(m.date) AS match_date,
    ts.stage_name AS stage,
    v.stadium_name,
    v.city
FROM matches m

JOIN teams ht
ON m.home_team_id = ht.team_id

JOIN teams at
ON m.away_team_id = at.team_id

JOIN tournament_stages ts
ON m.stage_id = ts.stage_id

JOIN venues v
ON m.venue_id = v.venue_id

ORDER BY
m.date,
m.kickoff_time_utc;