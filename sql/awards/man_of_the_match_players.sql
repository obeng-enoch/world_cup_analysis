WITH man_of_the_match AS (
    SELECT
        match_id,
        player_of_the_match_id
    FROM matches
    WHERE status = 'Completed'
      AND player_of_the_match_id IS NOT NULL
)

SELECT
    ps.player_name,
    t.fifa_code AS team,
    COUNT(DISTINCT motm.match_id) AS man_of_the_match_awards
FROM man_of_the_match AS motm
JOIN player_stats AS ps
    ON ps.player_id = motm.player_of_the_match_id
JOIN teams AS t
    ON t.team_id = ps.team_id
GROUP BY
    ps.player_id,
    ps.player_name,
    t.fifa_code
ORDER BY
    man_of_the_match_awards DESC,
    ps.player_name ASC
LIMIT 10;