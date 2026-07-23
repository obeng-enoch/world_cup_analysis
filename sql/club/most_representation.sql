-- 1) Most represented clubs (players sent to the tournament)
SELECT
    sp.club_team,
    COUNT(*) AS players_sent,
    COUNT(DISTINCT sp.team_id) AS countries_represented
FROM squads_and_players AS sp
GROUP BY sp.club_team
ORDER BY players_sent DESC, countries_represented DESC
LIMIT 15;