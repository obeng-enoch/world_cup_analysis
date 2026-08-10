-- 1) Venue directory
SELECT
    v.stadium_name,
    v.city,
    v.country,
    v.capacity,
    v.elevation_meters
FROM venues AS v
ORDER BY v.capacity DESC;