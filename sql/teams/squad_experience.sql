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