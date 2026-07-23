-- 1) Matches officiated per referee
SELECT
    r.name AS referee,
    r.country,
    r.avg_cards_per_game AS pre_tournament_avg_cards,
    COUNT(*) AS matches_officiated
FROM matches AS m
JOIN referees AS r
    ON m.referee_id = r.referee_id
WHERE m.status = 'Completed'
GROUP BY r.referee_id, r.name, r.country, r.avg_cards_per_game
ORDER BY matches_officiated DESC;