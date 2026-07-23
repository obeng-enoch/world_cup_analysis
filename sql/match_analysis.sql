-- ==========================================================
-- MATCH ANALYSIS
-- ==========================================================
-- Purpose:
-- Match-level analytics for the FIFA World Cup 2026 dashboard.
--
-- Dashboard Page:
-- Matches
--
-- Data Sources:
-- - matches
-- - teams
-- - venues
-- - tournament_stages
-- - match_team_stats
-- - match_events
--
-- NOTE: written for SQLite. Uses JULIANDAY/strftime for date
-- work and || for string concatenation.
-- ==========================================================

-- ==========================================================
-- 1) Full Match Schedule   
-- ==========================================================
SELECT
    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,
    DATE(m.date) AS match_date,
    ts.stage_name AS stage,
    v.stadium_name,
    v.city
FROM matches m

JOIN teams ht
ON m.home_team_id = ht.team_id

JOIN teams at
ON m.away_team_id = at.team_id

JOIN tournament_stages ts
ON m.stage_id = ts.stage_id

JOIN venues v
ON m.venue_id = v.venue_id

ORDER BY
m.date,
m.kickoff_time_utc;

-- ==========================================================
-- 2) Biggest Wins
-- ==========================================================
SELECT

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    ts.stage_name AS stage,

    ABS(m.home_score-m.away_score) AS goal_difference

FROM matches m

JOIN teams ht
ON m.home_team_id=ht.team_id

JOIN teams at
ON m.away_team_id=at.team_id

JOIN tournament_stages ts
ON m.stage_id=ts.stage_id

WHERE m.status='Completed'

ORDER BY
goal_difference DESC,
(m.home_score+m.away_score) DESC

LIMIT 10;

-- ==========================================================
-- 3) Highest Scoring Matches
-- ==========================================================

SELECT

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    ts.stage_name AS stage,

    CAST(m.home_score+m.away_score AS INTEGER) AS total_goals

FROM matches m

JOIN teams ht
ON m.home_team_id=ht.team_id

JOIN teams at
ON m.away_team_id=at.team_id

JOIN tournament_stages ts
ON m.stage_id=ts.stage_id

WHERE m.status='Completed'

ORDER BY total_goals DESC

LIMIT 10;

-- ==========================================================
-- 4) Matches Decided by Penalties
-- ==========================================================
SELECT

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    CAST(m.home_penalty_score AS INTEGER)
    || '–'
    || CAST(m.away_penalty_score AS INTEGER)
    AS penalty_score,

    CASE

        WHEN m.home_penalty_score>m.away_penalty_score
        THEN ht.fifa_code

        ELSE at.fifa_code

    END AS penalty_winner,

    DATE(m.date) AS match_date,

    ts.stage_name AS stage


FROM matches m

JOIN teams ht
ON m.home_team_id=ht.team_id

JOIN teams at
ON m.away_team_id=at.team_id

JOIN tournament_stages ts
ON m.stage_id=ts.stage_id

WHERE m.result_type='Penalties'

ORDER BY m.date;

-- 5) Biggest upsets (lower FIFA ranking beats higher-ranked opponent)
-- ==========================================================

SELECT

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    CASE
        WHEN m.home_score > m.away_score THEN ht.fifa_code
        WHEN m.away_score > m.home_score THEN at.fifa_code
    END AS winner,

    ABS(
        ht.fifa_ranking_pre_tournament -
        at.fifa_ranking_pre_tournament
    ) AS ranking_gap,

    ts.stage_name AS stage,

    DATE(m.date) AS match_date

FROM matches m

JOIN teams ht
ON m.home_team_id=ht.team_id

JOIN teams at
ON m.away_team_id=at.team_id

JOIN tournament_stages ts
ON m.stage_id=ts.stage_id

WHERE
m.status='Completed'

AND (

(ht.fifa_ranking_pre_tournament >
at.fifa_ranking_pre_tournament
AND m.home_score>m.away_score)

OR

(at.fifa_ranking_pre_tournament >
ht.fifa_ranking_pre_tournament
AND m.away_score>m.home_score)

)

ORDER BY ranking_gap DESC

LIMIT 10;

-- ==========================================================
-- SECTION B — GOAL TIMING
-- ==========================================================

-- 6) Goals by 15-minute window
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
    COUNT(*) AS goals
FROM match_events AS me
WHERE me.event_type = 'Goal'
GROUP BY time_window
ORDER BY MIN(me.minute) ASC;

-- 7) Late goals (85th minute or later)
SELECT

        ps.player_name,

    t.fifa_code,

    me.minute || '''' AS minute,

    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code
    AS match,

    DATE(m.date) AS match_date,

    ts.stage_name

FROM match_events AS me
JOIN matches AS m
    ON me.match_id = m.match_id
JOIN teams AS t
    ON me.team_id = t.team_id
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
JOIN player_stats AS ps
    ON me.player_id = ps.player_id
WHERE me.event_type = 'Goal' AND me.minute >= 85
ORDER BY me.minute DESC;

-- ==========================================================
-- SECTION C — VENUES
-- ==========================================================

-- 9) Matches and goals per venue
SELECT
    v.stadium_name,
    v.city,
    v.country,
    v.capacity,
    COUNT(*) AS matches_hosted,
    SUM(m.home_score + m.away_score) AS total_goals,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY v.venue_id, v.stadium_name, v.city, v.country, v.capacity
ORDER BY matches_hosted DESC, avg_goals_per_match DESC;

-- ==========================================================
-- SECTION D — STAGES
-- ==========================================================

-- 11) Matches and goals per stage
SELECT
    ts.stage_name AS stage,
    COUNT(*) AS matches_played,
    SUM(m.home_score + m.away_score) AS total_goals,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match
FROM matches AS m
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
WHERE m.status = 'Completed'
GROUP BY ts.stage_id, ts.stage_name, ts.is_knockout
ORDER BY ts.stage_id ASC;


-- 13) Most/least possession-dominant matches
SELECT
    ht.fifa_code
    || ' '
    || CAST(m.home_score AS INTEGER)
    || '–'
    || CAST(m.away_score AS INTEGER)
    || ' '
    || at.fifa_code AS match,

    ht.fifa_code
    || ' '
    || CAST(home_stats.possession_pct AS INTEGER)
    || '–'
    || CAST(away_stats.possession_pct AS INTEGER)
    || ' '
    || at.fifa_code AS possession,

    ABS(home_stats.possession_pct - away_stats.possession_pct) AS possession_gap

FROM matches AS m
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
JOIN match_team_stats AS home_stats
    ON home_stats.match_id = m.match_id AND home_stats.team_id = m.home_team_id
JOIN match_team_stats AS away_stats
    ON away_stats.match_id = m.match_id AND away_stats.team_id = m.away_team_id
WHERE m.status = 'Completed'
ORDER BY possession_gap DESC
LIMIT 10;