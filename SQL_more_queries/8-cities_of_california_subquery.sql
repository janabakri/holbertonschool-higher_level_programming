-- 8-cities_of_california_subquery.sql
-- This script lists all cities of California from hbtn_0d_usa without using JOIN
-- Task 8: Cities of California

SELECT id, name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
)
ORDER BY id ASC;
