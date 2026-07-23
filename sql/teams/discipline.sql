-- 6) Team card totals, with matches_played reflecting actual
-- team matches (from `matches`), not summed player appearances
WITH team_matches AS (
    SELECT match_id, home_team_id AS team_id
    FROM matches
    WHERE status = 'Completed'

    UNION ALL

    SELECT match_id, away_team_id AS team_id
    FROM matches
    WHERE status = 'Completed'
),

team_match_counts AS (
    SELECT
        team_id,
        COUNT(DISTINCT match_id) AS matches_played
    FROM team_matches
    GROUP BY team_id
)

SELECT
    t.fifa_code AS team,
    SUM(ps.yellow_cards) AS total_yellow_cards,
    SUM(ps.red_cards) AS total_red_cards,
    tmc.matches_played,
    ROUND(
        SUM(ps.yellow_cards + ps.red_cards) * 1.0 / NULLIF(tmc.matches_played, 0),
    2) AS cards_per_match
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
JOIN team_match_counts AS tmc
    ON ps.team_id = tmc.team_id
GROUP BY t.fifa_code, tmc.matches_played
ORDER BY total_yellow_cards DESC, total_red_cards DESC;