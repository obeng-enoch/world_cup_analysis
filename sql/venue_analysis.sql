-- ==========================================================
-- VENUE ANALYSIS
-- ==========================================================
-- Purpose:
-- Stadium/venue-level analytics for the FIFA World Cup 2026
-- dashboard — hosting load, scoring patterns, elevation
-- effects, and match-day style by venue.
--
-- Dashboard Page:
-- Venues
--
-- Data Sources:
-- - venues
-- - matches
-- - teams
-- - tournament_stages
-- - match_team_stats
--
-- NOTE: written for SQLite.
-- ==========================================================

-- ==========================================================
-- SECTION A — VENUE PROFILE
-- ==========================================================

-- 1) Venue directory
SELECT
    v.stadium_name,
    v.city,
    v.country,
    v.capacity,
    v.elevation_meters
FROM venues AS v
ORDER BY v.capacity DESC;

-- 2) Matches hosted per country/city
SELECT
    v.country,
    v.city,
    COUNT(DISTINCT v.venue_id) AS venues_used,
    COUNT(m.match_id) AS matches_hosted
FROM venues AS v
JOIN matches AS m
    ON v.venue_id = m.venue_id
WHERE m.status = 'Completed'
GROUP BY v.country, v.city
ORDER BY matches_hosted DESC;

-- ==========================================================
-- SECTION B — MATCH LOAD & SCORING
-- ==========================================================

-- 3) Matches, goals, and average goals per venue
SELECT
    v.stadium_name,
    v.city,
    v.country,
    COUNT(*) AS matches_hosted,
    SUM(m.home_score + m.away_score) AS total_goals,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY v.venue_id, v.stadium_name, v.city, v.country
ORDER BY avg_goals_per_match DESC, matches_hosted DESC
LIMIT 10;

-- 4) Highest-scoring single match per venue
SELECT
    v.stadium_name,
    m.match_id,
    m.date,
    ht.fifa_code || ' ' || m.home_score || '-' || m.away_score || ' ' || at.fifa_code AS scoreline,
    (m.home_score + m.away_score) AS total_goals
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
WHERE m.status = 'Completed'
    AND (m.home_score + m.away_score) = (
        SELECT MAX(m2.home_score + m2.away_score)
        FROM matches AS m2
        WHERE m2.venue_id = v.venue_id AND m2.status = 'Completed'
    )
ORDER BY total_goals DESC;

-- 5) Stage distribution per venue (group stage vs knockout load)
SELECT
    v.stadium_name,
    ts.stage_name AS stage,
    COUNT(*) AS matches_hosted
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
JOIN tournament_stages AS ts
    ON m.stage_id = ts.stage_id
GROUP BY v.stadium_name, ts.stage_name
ORDER BY v.stadium_name ASC, matches_hosted DESC;

-- ==========================================================
-- SECTION C — ELEVATION EFFECTS
-- ==========================================================

-- 6) Goals and xG accuracy by elevation band
SELECT
    CASE
        WHEN v.elevation_meters < 500 THEN 'Low (<500m)'
        WHEN v.elevation_meters < 1500 THEN 'Mid (500-1500m)'
        ELSE 'High (1500m+)'
    END AS elevation_band,
    COUNT(*) AS matches_played,
    ROUND(AVG(m.home_score + m.away_score), 2) AS avg_goals_per_match,
    ROUND(AVG(m.home_xg + m.away_xg), 2) AS avg_combined_xg
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY elevation_band
ORDER BY AVG(v.elevation_meters) ASC;

-- 7) Venues ranked by elevation (context table)
SELECT
    v.stadium_name,
    v.city,
    v.country,
    v.elevation_meters
FROM venues AS v
ORDER BY v.elevation_meters DESC;

-- ==========================================================
-- SECTION D — MATCH-DAY STYLE BY VENUE
-- ==========================================================

-- 8) Average possession, corners, fouls, offsides per venue
SELECT
    v.stadium_name,
    COUNT(DISTINCT m.match_id) AS matches_played,
    ROUND(AVG(mts.possession_pct), 2) AS avg_possession_pct,
    ROUND(AVG(mts.corners), 2) AS avg_corners,
    ROUND(AVG(mts.fouls), 2) AS avg_fouls,
    ROUND(AVG(mts.offsides), 2) AS avg_offsides
FROM match_team_stats AS mts
JOIN matches AS m
    ON mts.match_id = m.match_id
JOIN venues AS v
    ON m.venue_id = v.venue_id
WHERE m.status = 'Completed'
GROUP BY v.venue_id, v.stadium_name
ORDER BY avg_fouls DESC
LIMIT 10;

-- 9) Venues with the most one-sided possession matches
SELECT
    v.stadium_name,
    m.match_id,
    m.date,
    ht.fifa_code AS home_team,
    home_stats.possession_pct AS home_possession_pct,
    at.fifa_code AS away_team,
    away_stats.possession_pct AS away_possession_pct,
    ABS(home_stats.possession_pct - away_stats.possession_pct) AS possession_gap
FROM matches AS m
JOIN venues AS v
    ON m.venue_id = v.venue_id
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