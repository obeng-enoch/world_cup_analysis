-- ==========================================================
-- EVENT ANALYSIS
-- ==========================================================
-- Purpose:
-- Analytics on the raw match_events feed for the FIFA World
-- Cup 2026 dashboard — event-type breakdowns, card timing,
-- substitution patterns, own goals, and match intensity.
-- Complements match_analysis.sql (which focuses on goal
-- timing specifically) by covering the full event stream.
--
-- Dashboard Page:
-- Events
--
-- Data Sources:
-- - match_events
-- - matches
-- - teams
-- - tournament_stages
-- - player_stats
--
-- NOTE: written for SQLite. Assumes match_events.event_type
-- includes 'Goal', 'Own Goal', 'Yellow Card', 'Red Card', and
-- 'Substitution' values. Run:
--   SELECT DISTINCT event_type FROM match_events;
-- first to confirm the actual strings your ETL writes, and
-- adjust the WHERE/CASE clauses below if they differ.
-- ==========================================================

-- ==========================================================
-- SECTION A — EVENT TYPE OVERVIEW
-- ==========================================================

-- 1) Event counts by type
SELECT
    me.event_type,
    COUNT(*) AS total_events
FROM match_events AS me
GROUP BY me.event_type
ORDER BY total_events DESC;

-- 2) Average events per match by type
WITH match_count AS (
    SELECT COUNT(*) AS total_matches
    FROM matches
    WHERE status = 'Completed'
)
SELECT
    me.event_type,
    COUNT(*) AS total_events,
    ROUND(COUNT(*) * 1.0 / (SELECT total_matches FROM match_count), 2) AS avg_events_per_match
FROM match_events AS me
JOIN matches AS m
    ON me.match_id = m.match_id
WHERE m.status = 'Completed'
GROUP BY me.event_type
ORDER BY avg_events_per_match DESC;

-- ==========================================================
-- SECTION B — CARD EVENTS
-- ==========================================================

-- 3) Card timing distribution (15-minute windows)
SELECT
    CASE
        WHEN me.minute <= 15 THEN '0-15'
        WHEN me.minute <= 30 THEN '16-30'
        WHEN me.minute <= 45 THEN '31-45'
        WHEN me.minute <= 60 THEN '46-60'
        WHEN me.minute <= 75 THEN '61-75'
        WHEN me.minute <= 90 THEN '76-90'
        ELSE '90+'
    END AS time_window,
    SUM(CASE WHEN me.event_type = 'Yellow Card' THEN 1 ELSE 0 END) AS yellow_cards,
    SUM(CASE WHEN me.event_type = 'Red Card' THEN 1 ELSE 0 END) AS red_cards
FROM match_events AS me
WHERE me.event_type IN ('Yellow Card', 'Red Card')
GROUP BY time_window
ORDER BY MIN(me.minute) ASC;

-- 4) Players carded more than once in the same match
SELECT
    ps.player_name,
    t.fifa_code AS team,
    m.match_id,
    m.date,
    COUNT(*) AS cards_in_match,
    GROUP_CONCAT(me.event_type || ' (' || me.minute || ')') AS card_detail
FROM match_events AS me
JOIN matches AS m
    ON me.match_id = m.match_id
JOIN teams AS t
    ON me.team_id = t.team_id
JOIN player_stats AS ps
    ON me.player_id = ps.player_id
WHERE me.event_type IN ('Yellow Card', 'Red Card')
GROUP BY ps.player_name, t.fifa_code, m.match_id, m.date
HAVING COUNT(*) > 1
ORDER BY cards_in_match DESC;