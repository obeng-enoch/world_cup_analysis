-- 9) Pre-tournament ranking vs Elo rating (context table, no ordering bias)
SELECT
    t.fifa_code AS team,
    t.fifa_ranking_pre_tournament,
    t.elo_rating,
    t.confederation,
    t.manager_name
FROM teams AS t
ORDER BY t.fifa_ranking_pre_tournament ASC;