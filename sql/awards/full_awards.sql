-- 1) Full awards list, in a sensible display order
SELECT
    award_name,
    player_name,
    team,
    club
FROM tournament_awards
ORDER BY award_id;