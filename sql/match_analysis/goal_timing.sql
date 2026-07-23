-- 6) Goals by 15-minute window
SELECT
    CASE
        WHEN me.minute <= 15 THEN '0-15'
        WHEN me.minute <= 30 THEN '16-30'
        WHEN me.minute <= 45 THEN '31-45'
        WHEN me.minute <= 60 THEN '46-60'
        WHEN me.minute <= 75 THEN '61-75'
        WHEN me.minute <= 90 THEN '76-90'
        ELSE '90+'
    END AS time_window,
    COUNT(*) AS goals
FROM match_events AS me
WHERE me.event_type = 'Goal'
GROUP BY time_window
ORDER BY MIN(me.minute) ASC;