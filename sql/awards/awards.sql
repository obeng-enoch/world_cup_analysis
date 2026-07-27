-- 1) Full awards list, in a sensible display order
SELECT
    player_name,
    award_name,
    team
FROM tournament_awards
ORDER BY award_id;