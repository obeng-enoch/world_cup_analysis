-- ==========================================================
-- PLAYER ANALYSIS
-- ==========================================================
-- Purpose:
-- Individual player performance analytics for the FIFA World
-- Cup 2026 dashboard.
--
-- Dashboard Page:
-- Players
--
-- Data Sources:
-- - player_stats
-- - squads_and_players
-- - teams
-- - matches
-- - match_events
-- - tournament_stages
-- ==========================================================
-- SECTION A — SCORING
-- ==========================================================

-- 1. top goal scorers
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.goals,
    ps.assists,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.goals > 0
ORDER BY 
    ps.goals DESC, 
    ps.minutes_played ASC
LIMIT 10;

-- 2. goals per 90 minutes
SELECT
	ps.player_name,
	t.fifa_code AS team,
	ps.goals,
	ps.minutes_played,
	ROUND(CASE
		WHEN ps.minutes_played > 0 THEN (ps.goals * 90.0) / ps.minutes_played
		ELSE 0
	END, 2) AS goals_per_90
FROM player_stats AS ps
JOIN teams AS t
	ON ps.team_id = t.team_id
WHERE minutes_played > 0 AND goals > 0
ORDER BY goals_per_90 DESC, goals DESC
LIMIT 10;

-- 3. players who scored hat-tricks
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ht.fifa_code || ' VS ' || at.fifa_code AS match,
    ts.stage_name AS stage,
    COUNT(*) AS goals
FROM match_events AS me
JOIN player_stats AS ps
    ON me.player_id = ps.player_id
JOIN teams AS t
    ON ps.team_id = t.team_id
JOIN matches AS m
    ON me.match_id = m.match_id
JOIN teams AS ht
    ON m.home_team_id = ht.team_id
JOIN teams AS at
    ON m.away_team_id = at.team_id
JOIN tournament_stages AS ts
	ON m.stage_id = ts.stage_id
WHERE me.event_type = 'Goal'
GROUP BY
    me.match_id,
    ps.player_id,
    ps.player_name,
    t.fifa_code,
    ht.fifa_code,
    at.fifa_code
HAVING COUNT(*) >= 3
ORDER BY
    goals DESC,
    ps.player_name;

-- 4. multi-goals matches(2+ goals)
SELECT
	ps.player_name,
	t.fifa_code AS team,
	ht.fifa_code || ' VS ' || at.fifa_code AS match,
	ts.stage_name AS stage,
	COUNT(*) AS goals
FROM match_events AS me
JOIN player_stats AS ps
	ON me.player_id = ps.player_id
JOIN teams AS t
	ON ps.team_id = t.team_id
JOIN matches AS m
	ON me.match_id = m.match_id
JOIN teams AS ht
	ON m.home_team_id = ht.team_id
JOIN teams AS at
	ON m.away_team_id = at.team_id
JOIN tournament_stages AS ts
	ON m.stage_id = ts.stage_id
WHERE me.event_type = 'Goal'
GROUP BY
	me.match_id,
	ps.player_id,
	ps.player_name,
	t.fifa_code,
	ht.fifa_code,
	at.fifa_code
HAVING COUNT(*) >= 2
ORDER BY
	goals DESC,
	ps.player_name;

-- ==========================================================
-- SECTION A — SCORING
-- ==========================================================

-- 5) Penalty goals
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.penalty_goals,
    ps.goals,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.penalty_goals > 0
ORDER BY
    ps.penalty_goals DESC,
    ps.goals DESC,
    ps.minutes_played ASC
LIMIT 10;

-- 6) Own goals
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.own_goals,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.own_goals > 0
ORDER BY
    ps.own_goals DESC,
    ps.matches_played DESC
LIMIT 10;

-- ==========================================================
-- SECTION B — CREATIVITY
-- ==========================================================

-- 7) Top assist providers
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.assists,
    ps.goals,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.assists > 0
ORDER BY
    ps.assists DESC,
    ps.goals DESC,
    ps.minutes_played ASC
LIMIT 10;

-- 8) Goal contributions (Goals + Assists)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.goals,
    ps.assists,
    (ps.goals + ps.assists) AS goal_contributions,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE (ps.goals + ps.assists) > 0
ORDER BY
    goal_contributions DESC,
    ps.goals DESC,
    ps.assists DESC
LIMIT 10;

-- 9) Goal contributions per 90
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.goals,
    ps.assists,
    (ps.goals + ps.assists) AS goal_contributions,
    ps.minutes_played,
    ROUND(CASE
        WHEN ps.minutes_played > 0 THEN ((ps.goals + ps.assists) * 90.0) / ps.minutes_played
        ELSE 0
    END, 2) AS goal_contributions_per_90
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.minutes_played > 0 AND (ps.goals + ps.assists) > 0
ORDER BY
    goal_contributions_per_90 DESC,
    goal_contributions DESC
LIMIT 10;

-- ==========================================================
-- SECTION C — PLAYING TIME
-- ==========================================================

-- 10) Most appearances
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.matches_played,
    ps.matches_started,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.matches_played > 0
ORDER BY
    ps.matches_played DESC,
    ps.minutes_played DESC
LIMIT 10;

-- 11) Most starts
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.matches_started,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.matches_started > 0
ORDER BY
    ps.matches_started DESC,
    ps.minutes_played DESC
LIMIT 10;

-- 12) Most minutes played
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.minutes_played,
    ps.matches_played,
    ps.matches_started
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.minutes_played > 0
ORDER BY
    ps.minutes_played DESC,
    ps.matches_played DESC
LIMIT 10;

-- ==========================================================
-- SECTION D — DISCIPLINE
-- ==========================================================

-- 13) Most yellow cards
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.yellow_cards,
    ps.red_cards,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.yellow_cards > 0
ORDER BY
    ps.yellow_cards DESC,
    ps.red_cards DESC,
    ps.minutes_played ASC
LIMIT 10;

-- 14) Most red cards
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.red_cards,
    ps.yellow_cards,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.red_cards > 0
ORDER BY
    ps.red_cards DESC,
    ps.yellow_cards DESC,
    ps.minutes_played ASC
LIMIT 10;

-- ==========================================================
-- SECTION E — GOALKEEPING
-- ==========================================================

-- 15) Most clean sheets
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.position,
    ps.clean_sheets,
    ps.goals_conceded,
    ps.saves,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.position = 'GK' AND ps.clean_sheets > 0
ORDER BY
    ps.clean_sheets DESC,
    ps.matches_played DESC,
    ps.minutes_played DESC
LIMIT 10;

-- 16) Most saves
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.position,
    ps.saves,
    ps.clean_sheets,
    ps.goals_conceded,
    ps.matches_played,
    ps.minutes_played
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.position = 'GK' AND ps.saves > 0
ORDER BY
    ps.saves DESC,
    ps.clean_sheets DESC,
    ps.minutes_played DESC
LIMIT 10;

-- 17) Lowest goals conceded (minimum minutes threshold)
SELECT
    ps.player_name,
    t.fifa_code AS team,
    ps.position,
    ps.goals_conceded,
    ps.minutes_played,
    ps.clean_sheets,
    ps.saves
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
WHERE ps.position = 'GK' AND ps.minutes_played >= 180
ORDER BY
    ps.goals_conceded ASC,
    ps.minutes_played DESC
LIMIT 10;