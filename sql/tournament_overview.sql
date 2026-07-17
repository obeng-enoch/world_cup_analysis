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

-- KPI 5: Completed Matches
SELECT COUNT(*) AS completed_matches
FROM matches
WHERE status = 'Completed';

-- KPI 6: Upcoming Matches
SELECT COUNT(*) AS upcoming_matches
FROM matches
WHERE status <> 'Completed';

-- KPI 7: Total Goals
SELECT
    SUM(home_score + away_score) AS total_goals
FROM matches
WHERE status = 'Completed';

-- KPI 8: Average Goals Per Match
SELECT
    ROUND(AVG(home_score + away_score), 2) AS average_goals_per_match
FROM matches
WHERE status = 'Completed';