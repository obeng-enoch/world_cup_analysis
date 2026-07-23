-- 6) Most-used non-starters (impact substitutes)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    COUNT(*) AS appearances_off_bench,
    SUM(ml.minutes_played) AS total_bench_minutes,
    ROUND(AVG(ml.minutes_played), 2) AS avg_minutes_per_appearance
FROM match_lineups AS ml
JOIN teams AS t
    ON ml.team_id = t.team_id
JOIN player_stats AS ps
    ON ml.player_id = ps.player_id
WHERE ml.is_starting_xi = 0 AND ml.minutes_played > 0
GROUP BY ps.player_name, t.fifa_code
ORDER BY appearances_off_bench DESC, total_bench_minutes DESC
LIMIT 10;