-- 6) Goals and assists contributed by club
SELECT
    sp.club_team,
    COUNT(DISTINCT sp.player_id) AS players_sent,
    SUM(ps.goals) AS goals,
    SUM(ps.assists) AS assists,
    SUM(ps.goals + ps.assists) AS goal_contributions
FROM squads_and_players AS sp
JOIN player_stats AS ps
    ON sp.player_id = ps.player_id
GROUP BY sp.club_team
ORDER BY goal_contributions DESC, goals DESC
LIMIT 20;