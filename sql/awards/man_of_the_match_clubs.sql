WITH man_of_the_match AS (
    SELECT
        match_id,
        player_of_the_match_id
    FROM matches
    WHERE status = 'Completed'
      AND player_of_the_match_id IS NOT NULL
)

SELECT
    sp.club_team,
    COUNT(DISTINCT motm.match_id) AS man_of_the_match_awards,
    COUNT(DISTINCT ps.player_id) AS winning_players
FROM man_of_the_match AS motm
JOIN player_stats AS ps
    ON ps.player_id = motm.player_of_the_match_id
JOIN squads_and_players AS sp
    ON sp.player_id = ps.player_id
GROUP BY
    sp.club_team
ORDER BY
    man_of_the_match_awards DESC,
    winning_players DESC,
    sp.club_team ASC
LIMIT 10;