SELECT
    CASE
        WHEN result_type = 'Regular'
             AND home_score = away_score
            THEN 'Draw in 90 Minutes'

        WHEN result_type = 'Regular'
             AND home_score <> away_score
            THEN 'Win in 90 Minutes'

        WHEN result_type = 'AET'
            THEN 'Win in Extra Time'

        WHEN result_type = 'Penalties'
            THEN 'Win on Penalties'
    END AS result_type,

    COUNT(*) AS matches

FROM matches

GROUP BY
    CASE
        WHEN result_type = 'Regular'
             AND home_score = away_score
            THEN 'Draw in 90 Minutes'

        WHEN result_type = 'Regular'
             AND home_score <> away_score
            THEN 'Win in 90 Minutes'

        WHEN result_type = 'AET'
            THEN 'Win in Extra Time'

        WHEN result_type = 'Penalties'
            THEN 'Win on Penalties'
    END

ORDER BY matches DESC;