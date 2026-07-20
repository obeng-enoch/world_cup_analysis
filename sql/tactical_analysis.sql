-- ==========================================================
-- TACTICAL ANALYSIS
-- ==========================================================
-- Purpose:
-- Tactics and playing-style analytics for the FIFA World Cup
-- 2026 dashboard — formations/positions used, possession
-- style, squad rotation, and positional output.
--
-- Dashboard Page:
-- Tactics
--
-- Data Sources:
-- - match_lineups
-- - match_team_stats
-- - squads_and_players
-- - player_stats
-- - teams
-- - matches
--
-- NOTE: written for SQLite. Query 7 assumes
-- match_events.event_type includes a 'Substitution' value —
-- confirm the exact string your ETL writes (same caveat as
-- referee_analysis.sql) before trusting that one.
-- ==========================================================

-- ==========================================================
-- SECTION A — FORMATIONS & LINEUP USAGE
-- ==========================================================

-- 1) Most used tactical positions per team
SELECT
    t.fifa_code AS team,
    ml.tactical_position,
    COUNT(*) AS times_used
FROM match_lineups AS ml
JOIN teams AS t
    ON ml.team_id = t.team_id
WHERE ml.is_starting_xi = 1
GROUP BY t.fifa_code, ml.tactical_position
ORDER BY t.fifa_code ASC, times_used DESC;

-- 2) Squad rotation — distinct starters used per team
SELECT
    t.fifa_code AS team,
    COUNT(DISTINCT ml.match_id) AS matches_played,
    COUNT(DISTINCT ml.player_id) AS distinct_starters_used,
    ROUND(COUNT(DISTINCT ml.player_id) * 1.0 / NULLIF(COUNT(DISTINCT ml.match_id), 0), 2) AS starters_per_match
FROM match_lineups AS ml
JOIN teams AS t
    ON ml.team_id = t.team_id
WHERE ml.is_starting_xi = 1
GROUP BY t.fifa_code
ORDER BY distinct_starters_used DESC;

-- ==========================================================
-- SECTION B — POSSESSION & STYLE
-- ==========================================================

-- 3) Possession style tiers and results within each tier
WITH team_matches AS (
    SELECT m.match_id, m.home_team_id AS team_id,
           m.home_score AS goals_for, m.away_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.match_id, m.away_team_id AS team_id,
           m.away_score AS goals_for, m.home_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
)
SELECT
    CASE
        WHEN mts.possession_pct >= 60 THEN 'High possession (60%+)'
        WHEN mts.possession_pct >= 45 THEN 'Balanced (45-60%)'
        ELSE 'Low possession (<45%)'
    END AS possession_tier,
    COUNT(*) AS matches,
    SUM(CASE WHEN tm.goals_for > tm.goals_against THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN tm.goals_for = tm.goals_against THEN 1 ELSE 0 END) AS draws,
    SUM(CASE WHEN tm.goals_for < tm.goals_against THEN 1 ELSE 0 END) AS losses,
    ROUND(AVG(tm.goals_for), 2) AS avg_goals_for
FROM match_team_stats AS mts
JOIN team_matches AS tm
    ON mts.match_id = tm.match_id AND mts.team_id = tm.team_id
GROUP BY possession_tier
ORDER BY AVG(mts.possession_pct) DESC;

-- 4) Shooting efficiency per team (shots vs shots on target vs goals)
WITH team_matches AS (
    SELECT m.match_id, m.home_team_id AS team_id, m.home_score AS goals_for
    FROM matches AS m
    WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.match_id, m.away_team_id AS team_id, m.away_score AS goals_for
    FROM matches AS m
    WHERE m.status = 'Completed'
)
SELECT
    t.fifa_code AS team,
    SUM(mts.total_shots) AS total_shots,
    SUM(mts.shots_on_target) AS shots_on_target,
    SUM(tm.goals_for) AS goals_for,
    ROUND(SUM(mts.shots_on_target) * 100.0 / NULLIF(SUM(mts.total_shots), 0), 2) AS shot_accuracy_pct,
    ROUND(SUM(tm.goals_for) * 100.0 / NULLIF(SUM(mts.shots_on_target), 0), 2) AS conversion_of_shots_on_target_pct
FROM match_team_stats AS mts
JOIN team_matches AS tm
    ON mts.match_id = tm.match_id AND mts.team_id = tm.team_id
JOIN teams AS t
    ON mts.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY shot_accuracy_pct DESC
LIMIT 10;

-- ==========================================================
-- SECTION C — SUBSTITUTION & MINUTES PATTERNS
-- ==========================================================

-- 5) Starters vs bench minutes per team
SELECT
    t.fifa_code AS team,
    SUM(CASE WHEN ml.is_starting_xi = 1 THEN ml.minutes_played ELSE 0 END) AS starter_minutes,
    SUM(CASE WHEN ml.is_starting_xi = 0 THEN ml.minutes_played ELSE 0 END) AS bench_minutes,
    ROUND(
        SUM(CASE WHEN ml.is_starting_xi = 0 THEN ml.minutes_played ELSE 0 END) * 100.0
        / NULLIF(SUM(ml.minutes_played), 0),
    2) AS bench_minutes_pct
FROM match_lineups AS ml
JOIN teams AS t
    ON ml.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY bench_minutes_pct DESC;

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

-- ==========================================================
-- SECTION D — POSITIONAL OUTPUT
-- ==========================================================

-- 8) Goal contributions by position
SELECT
    ps.position,
    COUNT(DISTINCT ps.player_id) AS players,
    SUM(ps.goals) AS goals,
    SUM(ps.assists) AS assists,
    SUM(ps.goals + ps.assists) AS goal_contributions,
    ROUND((SUM(ps.goals + ps.assists) * 1.0) / NULLIF(COUNT(DISTINCT ps.player_id), 0), 2) AS contributions_per_player
FROM player_stats AS ps
GROUP BY ps.position
ORDER BY goal_contributions DESC;

-- 9) Discipline by position
SELECT
    ps.position,
    COUNT(DISTINCT ps.player_id) AS players,
    SUM(ps.yellow_cards) AS yellow_cards,
    SUM(ps.red_cards) AS red_cards,
    ROUND((SUM(ps.yellow_cards + ps.red_cards) * 1.0) / NULLIF(COUNT(DISTINCT ps.player_id), 0), 2) AS cards_per_player
FROM player_stats AS ps
GROUP BY ps.position
ORDER BY cards_per_player DESC;

-- ==========================================================
-- SECTION E — MATCH TEMPO & AGGRESSION
-- ==========================================================

-- 10) Fouls-to-cards ratio per team (aggression vs discipline)
WITH team_fouls AS (
    SELECT team_id, SUM(fouls) AS total_fouls
    FROM match_team_stats
    GROUP BY team_id
),
team_cards AS (
    SELECT team_id, SUM(yellow_cards + red_cards) AS total_cards
    FROM player_stats
    GROUP BY team_id
)
SELECT
    t.fifa_code AS team,
    tf.total_fouls,
    tc.total_cards,
    ROUND(tf.total_fouls * 1.0 / NULLIF(tc.total_cards, 0), 2) AS fouls_per_card
FROM teams AS t
JOIN team_fouls AS tf
    ON t.team_id = tf.team_id
JOIN team_cards AS tc
    ON t.team_id = tc.team_id
ORDER BY fouls_per_card ASC;

-- 11) Offside frequency per team (high-line/attacking-pace proxy)
SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    SUM(mts.offsides) AS total_offsides,
    ROUND(AVG(mts.offsides), 2) AS avg_offsides_per_match
FROM match_team_stats AS mts
JOIN teams AS t
    ON mts.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY avg_offsides_per_match DESC
LIMIT 10;