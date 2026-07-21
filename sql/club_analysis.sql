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

-- clubs whose players won the worldcup

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

-- ==========================================================
-- SECTION D — CLUB TOURNAMENT HONOURS
-- ==========================================================
-- Traces each team's tournament finish (Champion/Runner-up/Third
-- Place/etc.) back to the players' club sides via
-- squads_and_players.club_team. Mirrors the finish logic in
-- team_analysis.sql — kept in sync manually since SQLite has no
-- shared views across files in this project structure.

WITH team_matches AS (
    SELECT
        m.match_id,
        m.stage_id,
        m.home_team_id AS team_id,
        m.home_score AS goals_for,
        m.away_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'

    UNION ALL

    SELECT
        m.match_id,
        m.stage_id,
        m.away_team_id AS team_id,
        m.away_score AS goals_for,
        m.home_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
),

furthest_stage AS (
    SELECT
        team_id,
        MAX(stage_id) AS max_stage_id
    FROM team_matches
    GROUP BY team_id
),

final_match AS (
    SELECT
        tm.team_id,
        tm.stage_id,
        CASE
            WHEN tm.goals_for > tm.goals_against THEN 'Win'
            WHEN tm.goals_for < tm.goals_against THEN 'Loss'
            ELSE 'Draw'
        END AS result,
        ROW_NUMBER() OVER (PARTITION BY tm.team_id ORDER BY tm.match_id) AS rn
    FROM team_matches AS tm
    JOIN furthest_stage AS fs
        ON tm.team_id = fs.team_id
        AND tm.stage_id = fs.max_stage_id
),

team_finish AS (
    SELECT
        fm.team_id,
        CASE
            WHEN fm.stage_id = 7 AND fm.result = 'Win'             THEN 'Champion'
            WHEN fm.stage_id = 7 AND fm.result IN ('Loss','Draw')  THEN 'Runner-up'
            WHEN fm.stage_id = 6 AND fm.result = 'Win'             THEN 'Third Place'
            WHEN fm.stage_id = 6 AND fm.result IN ('Loss','Draw')  THEN 'Fourth Place'
            WHEN fm.stage_id = 5                                   THEN 'Semi-finalist'
            WHEN fm.stage_id = 4                                   THEN 'Quarter-finalist'
            WHEN fm.stage_id = 3                                   THEN 'Round of 16'
            WHEN fm.stage_id = 2                                   THEN 'Round of 32'
            WHEN fm.stage_id = 1                                   THEN 'Eliminated - Group Stage'
            ELSE 'Unknown'
        END AS tournament_finish
    FROM final_match AS fm
    WHERE fm.rn = 1
)

-- 10) Clubs whose players won the World Cup (Champion squad),
-- highest to lowest
SELECT
    sp.club_team,
    COUNT(*) AS champion_players
FROM squads_and_players AS sp
JOIN team_finish AS tf
    ON sp.team_id = tf.team_id
WHERE tf.tournament_finish = 'Champion'
GROUP BY sp.club_team
ORDER BY champion_players DESC;

-- 11) Club medal table — Gold (Champion), Silver (Runner-up),
-- Bronze (Third Place) players by club, ordered by total medals
WITH team_matches AS ( /* same as above */
    SELECT m.match_id, m.stage_id, m.home_team_id AS team_id,
           m.home_score AS goals_for, m.away_score AS goals_against
    FROM matches AS m WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.match_id, m.stage_id, m.away_team_id AS team_id,
           m.away_score AS goals_for, m.home_score AS goals_against
    FROM matches AS m WHERE m.status = 'Completed'
),
furthest_stage AS (
    SELECT team_id, MAX(stage_id) AS max_stage_id
    FROM team_matches GROUP BY team_id
),
final_match AS (
    SELECT tm.team_id, tm.stage_id,
        CASE
            WHEN tm.goals_for > tm.goals_against THEN 'Win'
            WHEN tm.goals_for < tm.goals_against THEN 'Loss'
            ELSE 'Draw'
        END AS result,
        ROW_NUMBER() OVER (PARTITION BY tm.team_id ORDER BY tm.match_id) AS rn
    FROM team_matches AS tm
    JOIN furthest_stage AS fs
        ON tm.team_id = fs.team_id AND tm.stage_id = fs.max_stage_id
),
team_finish AS (
    SELECT fm.team_id,
        CASE
            WHEN fm.stage_id = 7 AND fm.result = 'Win'             THEN 'Champion'
            WHEN fm.stage_id = 7 AND fm.result IN ('Loss','Draw')  THEN 'Runner-up'
            WHEN fm.stage_id = 6 AND fm.result = 'Win'             THEN 'Third Place'
            WHEN fm.stage_id = 6 AND fm.result IN ('Loss','Draw')  THEN 'Fourth Place'
            ELSE 'Other'
        END AS tournament_finish
    FROM final_match AS fm
    WHERE fm.rn = 1
)

SELECT
    sp.club_team,
    SUM(CASE WHEN tf.tournament_finish = 'Champion'    THEN 1 ELSE 0 END) AS gold,
    SUM(CASE WHEN tf.tournament_finish = 'Runner-up'   THEN 1 ELSE 0 END) AS silver,
    SUM(CASE WHEN tf.tournament_finish = 'Third Place' THEN 1 ELSE 0 END) AS bronze,
    SUM(CASE WHEN tf.tournament_finish IN ('Champion','Runner-up','Third Place') THEN 1 ELSE 0 END) AS total_medals
FROM squads_and_players AS sp
JOIN team_finish AS tf
    ON sp.team_id = tf.team_id
GROUP BY sp.club_team
HAVING total_medals > 0
ORDER BY total_medals DESC, gold DESC, silver DESC, bronze DESC;