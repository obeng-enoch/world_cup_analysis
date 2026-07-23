-- ==========================================================
-- TOURNAMENT AWARDS
-- ==========================================================
-- Purpose:
-- Individual and team awards for the FIFA World Cup 2026 —
-- manually curated (not derivable from match/player stats),
-- source of truth for the Awards dashboard page.
--
-- Dashboard Page:
-- Awards
--
-- Data Sources:
-- - Manually entered (no upstream table)
--
-- NOTE: written for SQLite.
-- ==========================================================

-- ==========================================================
-- SECTION A — TABLE DEFINITION
-- ==========================================================

DROP TABLE IF EXISTS tournament_awards;

CREATE TABLE tournament_awards (
    award_id INTEGER PRIMARY KEY,
    award_name TEXT NOT NULL,
    recipient_type TEXT NOT NULL,
    team TEXT NOT NULL,
    player_name TEXT,
    club TEXT
);

-- ==========================================================
-- SECTION B — DATA
-- ==========================================================

INSERT INTO tournament_awards (award_id, award_name, recipient_type, team, player_name, club) VALUES
(1, 'Golden Ball',        'Player', 'Spain',       'Rodri',            'Manchester City'),
(2, 'Silver Ball',        'Player', 'Argentina',   'Lionel Messi',     'Inter Miami CF'),
(3, 'Bronze Ball',        'Player', 'France',      'Kylian Mbappé',    'Real Madrid'),
(4, 'Golden Boot',        'Player', 'France',      'Kylian Mbappé',    'Real Madrid'),
(5, 'Silver Boot',        'Player', 'Argentina',   'Lionel Messi',     'Inter Miami CF'),
(6, 'Bronze Boot',        'Player', 'England',     'Jude Bellingham',  'Real Madrid'),
(7, 'Golden Glove',       'Player', 'Spain',       'Unai Simón',       'Athletic Club'),
(8, 'Best Young Player',  'Player', 'Spain',       'Pau Cubarsí',      'Barcelona'),
(9, 'Fair Play Award',    'Team',   'Netherlands', NULL,               NULL);

-- ==========================================================
-- SECTION C — DASHBOARD QUERY
-- ==========================================================

-- 1) Full awards list, in a sensible display order
SELECT
    award_name,
    player_name,
    team,
    club
FROM tournament_awards
ORDER BY award_id;

