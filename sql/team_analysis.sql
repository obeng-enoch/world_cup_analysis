-- ==========================================================
-- TEAM ANALYSIS
-- ==========================================================
-- Purpose:
-- Team-level performance analytics for the FIFA World
-- Cup 2026 dashboard.
--
-- Dashboard Page:
-- Teams
--
-- Data Sources:
-- - teams
-- - matches
-- - match_team_stats
-- - player_stats
-- - squads_and_players
-- - tournament_stages
-- ==========================================================
-- Shared building block: one row per team per completed match,
-- from that team's own perspective (goals for/against), by
-- unpivoting home/away rows out of `matches`. Re-used by
-- several queries below via CTE.
-- ==========================================================

-- ==========================================================
-- SECTION A — STANDINGS & RESULTS
-- ==========================================================

-- ==========================================================
-- SECTION B — ATTACK
-- ==========================================================

-- ==========================================================
-- 1) Highest Scoring Teams
-- ==========================================================
WITH team_attack AS (
    SELECT
        m.match_id,
        m.home_team_id AS team_id,
        m.home_score AS goals_for
    FROM matches AS m
    WHERE m.status = 'Completed'

    UNION ALL

    SELECT
        m.match_id,
        m.away_team_id,
        m.away_score
    FROM matches AS m
    WHERE m.status = 'Completed'
)

SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    SUM(ta.goals_for) AS goals,
    ROUND(AVG(ta.goals_for),2) AS goals_per_match,

    SUM(mts.total_shots) AS shots,
    SUM(mts.shots_on_target) AS shots_on_target,

    ROUND(
        CASE
            WHEN SUM(mts.total_shots) > 0
            THEN SUM(ta.goals_for) * 100.0 / SUM(mts.total_shots)
        END,
    2) AS shot_conversion_pct

FROM team_attack ta

JOIN match_team_stats mts
ON ta.match_id = mts.match_id
AND ta.team_id = mts.team_id

JOIN teams t
ON ta.team_id = t.team_id

GROUP BY t.fifa_code

ORDER BY
goals DESC,
goals_per_match DESC;

-- ==========================================================
-- 2) Most Clinical Teams
-- ==========================================================
WITH team_attack AS (

    SELECT
        m.match_id,
        m.home_team_id AS team_id,
        m.home_score AS goals_for
    FROM matches m
    WHERE m.status='Completed'

    UNION ALL

    SELECT
        m.match_id,
        m.away_team_id,
        m.away_score
    FROM matches m
    WHERE m.status='Completed'

)

SELECT

    t.fifa_code AS team,

    COUNT(*) AS matches_played,

    SUM(ta.goals_for) AS goals,

    SUM(mts.total_shots) AS shots,

    ROUND(
        SUM(ta.goals_for)*100.0 /
        NULLIF(SUM(mts.total_shots),0),
    2) AS shot_conversion_pct

FROM team_attack ta

JOIN match_team_stats mts
ON ta.match_id=mts.match_id
AND ta.team_id=mts.team_id

JOIN teams t
ON ta.team_id=t.team_id

GROUP BY t.fifa_code

HAVING SUM(mts.total_shots) >= 20

ORDER BY shot_conversion_pct DESC;

-- ==========================================================
-- 3) Most Aggressive Attacking Teams
-- ==========================================================
SELECT
    t.fifa_code AS team,

    COUNT(*) AS matches_played,

    SUM(mts.total_shots) AS total_shots,

    SUM(mts.shots_on_target) AS shots_on_target,

    ROUND(AVG(mts.total_shots),2) AS shots_per_match,

    ROUND(AVG(mts.shots_on_target),2) AS shots_on_target_per_match

FROM match_team_stats mts

JOIN matches m
ON mts.match_id=m.match_id

JOIN teams t
ON mts.team_id=t.team_id

WHERE m.status='Completed'

GROUP BY t.fifa_code

ORDER BY
total_shots DESC,
shots_on_target DESC;

-- ==========================================================
-- SECTION C — DEFENSE
-- ==========================================================

-- 4) Best defensive teams (goals conceded, clean sheets)
WITH team_matches AS (
    SELECT m.home_team_id AS team_id, m.away_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
    UNION ALL
    SELECT m.away_team_id AS team_id, m.home_score AS goals_against
    FROM matches AS m
    WHERE m.status = 'Completed'
)
SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    SUM(tm.goals_against) AS goals_against,
    ROUND(AVG(tm.goals_against), 2) AS goals_conceded_per_match,
    SUM(CASE WHEN tm.goals_against = 0 THEN 1 ELSE 0 END) AS clean_sheets
FROM team_matches AS tm
JOIN teams AS t
    ON tm.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY goals_conceded_per_match ASC, clean_sheets DESC
LIMIT 10;

-- ==========================================================
-- SECTION D — POSSESSION & STYLE
-- ==========================================================

-- 5) Average possession, corners, fouls, offsides per team
SELECT
    t.fifa_code AS team,
    COUNT(*) AS matches_played,
    ROUND(AVG(mts.possession_pct), 2) AS avg_possession_pct,
    ROUND(AVG(mts.corners), 2) AS avg_corners,
    ROUND(AVG(mts.fouls), 2) AS avg_fouls,
    ROUND(AVG(mts.offsides), 2) AS avg_offsides
FROM match_team_stats AS mts
JOIN matches AS m
    ON mts.match_id = m.match_id
JOIN teams AS t
    ON mts.team_id = t.team_id
WHERE m.status = 'Completed'
GROUP BY t.fifa_code
ORDER BY avg_possession_pct DESC;

-- ==========================================================
-- SECTION E — DISCIPLINE
-- ==========================================================

-- 6) Team card totals
SELECT
    t.fifa_code AS team,
    SUM(ps.yellow_cards) AS total_yellow_cards,
    SUM(ps.red_cards) AS total_red_cards,
    SUM(ps.matches_played) AS squad_matches_played,
    ROUND(SUM(ps.yellow_cards + ps.red_cards) * 1.0 / NULLIF(SUM(ps.matches_played), 0), 2) AS cards_per_match
FROM player_stats AS ps
JOIN teams AS t
    ON ps.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY total_yellow_cards DESC, total_red_cards DESC;

-- ==========================================================
-- SECTION F — SQUAD PROFILE
-- ==========================================================

-- 7) Squad market value
SELECT
    t.fifa_code AS team,
    COUNT(*) AS squad_size,
    ROUND(SUM(sp.market_value_eur), 2) AS total_market_value_eur,
    ROUND(AVG(sp.market_value_eur), 2) AS avg_market_value_eur
FROM squads_and_players AS sp
JOIN teams AS t
    ON sp.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY total_market_value_eur DESC;

-- 8) Squad experience (average caps, average age)
-- NOTE: age is computed against a fixed tournament reference date via
-- julianday() (SQLite); swap '2026-06-11' for the actual WC 2026 kickoff date.
SELECT
    t.fifa_code AS team,
    COUNT(*) AS squad_size,
    ROUND(AVG(sp.caps), 2) AS avg_caps,
    ROUND(AVG((JULIANDAY('2026-06-11') - JULIANDAY(sp.date_of_birth)) / 365.25), 2) AS avg_age
FROM squads_and_players AS sp
JOIN teams AS t
    ON sp.team_id = t.team_id
GROUP BY t.fifa_code
ORDER BY avg_caps DESC;

-- 9) Pre-tournament ranking vs Elo rating (context table, no ordering bias)
SELECT
    t.fifa_code AS team,
    t.fifa_ranking_pre_tournament,
    t.elo_rating,
    t.confederation,
    t.manager_name
FROM teams AS t
ORDER BY t.fifa_ranking_pre_tournament ASC;

SELECT stage_id, stage_name FROM tournament_stages

SELECT
match_id,
stage_id,
home_team_id,
away_team_id,
home_score,
away_score
FROM matches
LIMIT 10;