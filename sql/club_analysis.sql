-- ==========================================================
-- CLUB ANALYSIS
-- ==========================================================
-- Purpose:
-- Analytics on the club sides players belong to outside the
-- tournament (squads_and_players.club_team) — representation,
-- squad value, and how much tournament output traces back to
-- each club.
--
-- Dashboard Page:
-- Clubs
--
-- Data Sources:
-- - squads_and_players
-- - player_stats
-- - teams
--
-- NOTE: written for SQLite.
-- ==========================================================

-- ==========================================================
-- SECTION A — CLUB REPRESENTATION
-- ==========================================================

-- 1) Most represented clubs (players sent to the tournament)
SELECT
    sp.club_team,
    COUNT(*) AS players_sent,
    COUNT(DISTINCT sp.team_id) AS countries_represented
FROM squads_and_players AS sp
GROUP BY sp.club_team
ORDER BY players_sent DESC, countries_represented DESC
LIMIT 15;

-- 2) Clubs whose players represent the most different national teams
SELECT
    sp.club_team,
    COUNT(DISTINCT sp.team_id) AS countries_represented,
    COUNT(*) AS players_sent
FROM squads_and_players AS sp
GROUP BY sp.club_team
HAVING COUNT(DISTINCT sp.team_id) > 1
ORDER BY countries_represented DESC, players_sent DESC
LIMIT 10;

-- ==========================================================
-- SECTION B — CLUB SQUAD VALUE
-- ==========================================================

-- 4) Most valuable clubs by combined market value of players sent
SELECT
    sp.club_team,
    COUNT(*) AS players_sent,
    ROUND(SUM(sp.market_value_eur), 2) AS total_market_value_eur,
    ROUND(AVG(sp.market_value_eur), 2) AS avg_market_value_eur
FROM squads_and_players AS sp
GROUP BY sp.club_team
ORDER BY total_market_value_eur DESC
LIMIT 10;

-- 5) Most valuable individual player per club (top asset)
SELECT
    sp.club_team,
    sp.player_name,
    t.fifa_code AS team,
    sp.position,
    sp.market_value_eur
FROM squads_and_players AS sp
JOIN teams AS t
    ON sp.team_id = t.team_id
WHERE sp.market_value_eur = (
    SELECT MAX(sp2.market_value_eur)
    FROM squads_and_players AS sp2
    WHERE sp2.club_team = sp.club_team
)
ORDER BY sp.market_value_eur DESC
LIMIT 10;

-- ==========================================================
-- SECTION C — CLUB TOURNAMENT PERFORMANCE
-- ==========================================================
-- Attributes in-tournament output (goals, assists, minutes, cards)
-- back to the players' club sides via squads_and_players.club_team.

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

-- 7) Minutes played contributed by club (squad game-time footprint)
SELECT
    sp.club_team,
    COUNT(DISTINCT sp.player_id) AS players_sent,
    SUM(ps.minutes_played) AS total_minutes_played,
    ROUND(AVG(ps.minutes_played), 2) AS avg_minutes_per_player
FROM squads_and_players AS sp
JOIN player_stats AS ps
    ON sp.player_id = ps.player_id
GROUP BY sp.club_team
ORDER BY total_minutes_played DESC
LIMIT 10;

-- 8) Discipline record by club
SELECT
    sp.club_team,
    COUNT(DISTINCT sp.player_id) AS players_sent,
    SUM(ps.yellow_cards) AS total_yellow_cards,
    SUM(ps.red_cards) AS total_red_cards
FROM squads_and_players AS sp
JOIN player_stats AS ps
    ON sp.player_id = ps.player_id
GROUP BY sp.club_team
HAVING SUM(ps.yellow_cards + ps.red_cards) > 0
ORDER BY total_red_cards DESC, total_yellow_cards DESC
LIMIT 10;

-- 9) Goal contribution efficiency per club (contributions per player sent)
SELECT
    sp.club_team,
    COUNT(DISTINCT sp.player_id) AS players_sent,
    SUM(ps.goals + ps.assists) AS goal_contributions,
    ROUND((SUM(ps.goals + ps.assists) * 1.0) / COUNT(DISTINCT sp.player_id), 2) AS contributions_per_player
FROM squads_and_players AS sp
JOIN player_stats AS ps
    ON sp.player_id = ps.player_id
GROUP BY sp.club_team
HAVING COUNT(DISTINCT sp.player_id) >= 2
ORDER BY contributions_per_player DESC, goal_contributions DESC
LIMIT 10;