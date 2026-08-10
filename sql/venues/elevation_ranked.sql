-- 7) Venues ranked by elevation (context table)
SELECT
    v.stadium_name,
    v.city,
    v.country,
    v.elevation_meters
FROM venues AS v
ORDER BY v.elevation_meters DESC;