-- ==========================================================
-- REFEREE ANALYSIS
-- ==========================================================
-- Purpose:
-- Referee-level analytics for the FIFA World Cup 2026
-- dashboard — workload, card issuance, and how matches play
-- out under each official.
--
-- Dashboard Page:
-- Referees
--
-- Data Sources:
-- - referees
-- - matches
-- - teams
-- - tournament_stages
-- - match_team_stats
-- - match_events
--
-- NOTE: written for SQLite. Queries in Section B assume
-- match_events.event_type includes 'Yellow Card' and
-- 'Red Card' values (mirroring the 'Goal' value used in
-- player_analysis.sql) — confirm the exact strings your ETL
-- writes and adjust the WHERE/CASE clauses if they differ.
-- ==========================================================

-- ==========================================================
-- SECTION A — REFEREE PROFILE & WORKLOAD
-- ==========================================================

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

-- 2) Referees by country
SELECT
    r.country,
    COUNT(DISTINCT r.referee_id) AS referees_assigned,
    COUNT(m.match_id) AS matches_officiated
FROM referees AS r
LEFT JOIN matches AS m
    ON r.referee_id = m.referee_id AND m.status = 'Completed'
GROUP BY r.country
ORDER BY matches_officiated DESC;

-- ==========================================================
-- SECTION B — CARD ISSUANCE
-- ==========================================================

-- 3) Actual cards issued per referee vs pre-tournament reputation
WITH ref_cards AS (
    SELECT
        m.referee_id,
        SUM(CASE WHEN me.event_type = 'Yellow Card' THEN 1 ELSE 0 END) AS yellow_cards,
        SUM(CASE WHEN me.event_type = 'Red Card' THEN 1 ELSE 0 END) AS red_cards
    FROM matches AS m
    LEFT JOIN match_events AS me
        ON me.match_id = m.match_id AND me.event_type IN ('Yellow Card', 'Red Card')
    WHERE m.status = 'Completed'
    GROUP BY m.referee_id
),
ref_matches AS (
    SELECT referee_id, COUNT(*) AS matches_officiated
    FROM matches
    WHERE status = 'Completed'
    GROUP BY referee_id
)
SELECT
    r.name AS referee,
    r.country,
    rm.matches_officiated,
    rc.yellow_cards,
    rc.red_cards,
    ROUND((rc.yellow_cards + rc.red_cards) * 1.0 / NULLIF(rm.matches_officiated, 0), 2) AS actual_avg_cards_per_game,
    r.avg_cards_per_game AS pre_tournament_avg_cards,
    ROUND(
        ((rc.yellow_cards + rc.red_cards) * 1.0 / NULLIF(rm.matches_officiated, 0)) - r.avg_cards_per_game,
    2) AS cards_delta
FROM referees AS r
JOIN ref_matches AS rm
    ON r.referee_id = rm.referee_id
JOIN ref_cards AS rc
    ON r.referee_id = rc.referee_id
ORDER BY actual_avg_cards_per_game DESC;

-- 4) Referees who have shown a red card
SELECT
    r.name AS referee,
    r.country,
    m.match_id,
    m.date,
    ht.fifa_code || ' VS ' || at.fifa_code AS match,
    t.fifa_code AS carded_team,
    ps.player_name,
    me.minute
FROM match_events AS me
JOIN matches AS m
    ON me.match_id = m.match_id
JOIN referees AS r
    ON m.referee_id = r.referee_id
JOIN teams AS t
    ON me.team_id = t.team_id
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
JOIN player_stats AS ps
    ON me.player_id = ps.player_id
WHERE me.event_type = 'Red Card'
ORDER BY m.date ASC;

-- ==========================================================
-- SECTION C — MATCH OUTCOMES UNDER REFEREE
-- ==========================================================

-- 5) Average goals per match by referee
SELECT
    r.name AS referee,
    r.country,
    COUNT(*) AS matches_officiated,
    SUM(m.home_score + m.away_score) AS total_goals,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match
FROM matches AS m
JOIN referees AS r
    ON m.referee_id = r.referee_id
WHERE m.status = 'Completed'
GROUP BY r.referee_id, r.name, r.country
ORDER BY avg_goals_per_match DESC
LIMIT 10;

-- 6) Average fouls per match by referee
SELECT
    r.name AS referee,
    r.country,
    COUNT(DISTINCT m.match_id) AS matches_officiated,
    ROUND(AVG(match_fouls.total_fouls), 2) AS avg_fouls_per_match
FROM matches AS m
JOIN referees AS r
    ON m.referee_id = r.referee_id
JOIN (
    SELECT match_id, SUM(fouls) AS total_fouls
    FROM match_team_stats
    GROUP BY match_id
) AS match_fouls
    ON match_fouls.match_id = m.match_id
WHERE m.status = 'Completed'
GROUP BY r.referee_id, r.name, r.country
ORDER BY avg_fouls_per_match DESC
LIMIT 10;

-- ==========================================================
-- SECTION D — WORKLOAD BY STAGE
-- ==========================================================

-- 8) Matches officiated per referee by stage (trust in high-stakes games)
SELECT
    r.name AS referee,
    ts.stage_name AS stage,
    ts.is_knockout,
    COUNT(*) AS matches_officiated
FROM matches AS m
JOIN referees AS r
    ON m.referee_id = r.referee_id
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
GROUP BY r.referee_id, r.name, ts.stage_name, ts.is_knockout
ORDER BY r.name ASC, matches_officiated DESC;