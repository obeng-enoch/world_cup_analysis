-- 4) Highest-scoring single match per venue
SELECT
    v.stadium_name,
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