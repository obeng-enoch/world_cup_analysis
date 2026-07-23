-- ==========================================
-- TOURNAMENT OVERVIEW
-- ==========================================
-- Purpose:
-- Queries powering the homepage KPIs.
-- ==========================================

-- KPI 1: Total Teams
SELECT COUNT(*) AS total_teams
FROM teams;

-- KPI 2: Total Players
SELECT COUNT(*) AS total_players
FROM squads_and_players;

-- KPI 3: Total Clubs Represented
SELECT COUNT(DISTINCT club_team) AS total_clubs
FROM squads_and_players;

-- KPI 4: Total Matches
SELECT COUNT(*) AS total_matches
FROM matches;

-- KPI 5: Total Goals
SELECT
    SUM(home_score + away_score) AS total_goals
FROM matches
WHERE status = 'Completed';
