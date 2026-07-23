-- 5) Biggest upsets (lower FIFA ranking beats higher-ranked opponent)
-- ==========================================================

SELECT

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    CASE
        WHEN m.home_score > m.away_score THEN ht.fifa_code
        WHEN m.away_score > m.home_score THEN at.fifa_code
    END AS winner,

    ABS(
        ht.fifa_ranking_pre_tournament -
        at.fifa_ranking_pre_tournament
    ) AS ranking_gap,

    ts.stage_name AS stage,

    DATE(m.date) AS match_date

FROM matches m

JOIN teams ht
ON m.home_team_id=ht.team_id

JOIN teams at
ON m.away_team_id=at.team_id

JOIN tournament_stages ts
ON m.stage_id=ts.stage_id

WHERE
m.status='Completed'

AND (

(ht.fifa_ranking_pre_tournament >
at.fifa_ranking_pre_tournament
AND m.home_score>m.away_score)

OR

(at.fifa_ranking_pre_tournament >
ht.fifa_ranking_pre_tournament
AND m.away_score>m.home_score)

)

ORDER BY ranking_gap DESC

LIMIT 10;