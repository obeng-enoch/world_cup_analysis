-- 3) Actual cards issued per referee vs pre-tournament reputation
WITH ref_cards AS (
    SELECT
        m.referee_id,
        SUM(CASE WHEN me.event_type = 'Yellow Card' THEN 1 ELSE 0 END) AS yellow_cards,
        SUM(CASE WHEN me.event_type = 'Red Card' THEN 1 ELSE 0 END) AS red_cards
    FROM matches AS m
    LEFT JOIN match_events AS me
        ON me.match_id = m.match_id AND me.event_type IN ('Yellow Card', 'Red Card')
    WHERE m.status = 'Completed'
    GROUP BY m.referee_id
),
ref_matches AS (
    SELECT referee_id, COUNT(*) AS matches_officiated
    FROM matches
    WHERE status = 'Completed'
    GROUP BY referee_id
)
SELECT
    r.name AS referee,
    r.country,
    rm.matches_officiated,
    rc.yellow_cards,
    rc.red_cards,
    ROUND((rc.yellow_cards + rc.red_cards) * 1.0 / NULLIF(rm.matches_officiated, 0), 2) AS actual_avg_cards_per_game,
    r.avg_cards_per_game AS pre_tournament_avg_cards,
    ROUND(
        ((rc.yellow_cards + rc.red_cards) * 1.0 / NULLIF(rm.matches_officiated, 0)) - r.avg_cards_per_game,
    2) AS cards_delta
FROM referees AS r
JOIN ref_matches AS rm
    ON r.referee_id = rm.referee_id
JOIN ref_cards AS rc
    ON r.referee_id = rc.referee_id
ORDER BY actual_avg_cards_per_game DESC;