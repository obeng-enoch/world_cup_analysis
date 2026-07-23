-- Most red cards
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.red_cards,
    ps.yellow_cards,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t ON ps.team_id = t.team_id
WHERE ps.red_cards > 0
ORDER BY ps.red_cards DESC, ps.yellow_cards DESC, ps.minutes_played ASC
LIMIT 10;