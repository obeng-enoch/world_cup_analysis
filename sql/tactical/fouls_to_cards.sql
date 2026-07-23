-- 10) Fouls-to-cards ratio per team (aggression vs discipline)
WITH team_fouls AS (
    SELECT team_id, SUM(fouls) AS total_fouls
    FROM match_team_stats
    GROUP BY team_id
),
team_cards AS (
    SELECT team_id, SUM(yellow_cards + red_cards) AS total_cards
    FROM player_stats
    GROUP BY team_id
)
SELECT
    t.fifa_code AS team,
    tf.total_fouls,
    tc.total_cards,
    ROUND(tf.total_fouls * 1.0 / NULLIF(tc.total_cards, 0), 2) AS fouls_per_card
FROM teams AS t
JOIN team_fouls AS tf
    ON t.team_id = tf.team_id
JOIN team_cards AS tc
    ON t.team_id = tc.team_id
ORDER BY fouls_per_card ASC;