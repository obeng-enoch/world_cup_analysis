-- ==========================================================
-- 4) Matches Decided by Penalties
-- ==========================================================
SELECT

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    CAST(m.home_penalty_score AS INTEGER)
    || '–'
    || CAST(m.away_penalty_score AS INTEGER)
    AS penalty_score,

    CASE

        WHEN m.home_penalty_score>m.away_penalty_score
        THEN ht.fifa_code

        ELSE at.fifa_code

    END AS penalty_winner,

    DATE(m.date) AS match_date,

    ts.stage_name AS stage


FROM matches m

JOIN teams ht
ON m.home_team_id=ht.team_id

JOIN teams at
ON m.away_team_id=at.team_id

JOIN tournament_stages ts
ON m.stage_id=ts.stage_id

WHERE m.result_type='Penalties'

ORDER BY m.date;