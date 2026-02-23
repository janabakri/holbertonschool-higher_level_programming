-- 15-groups.sql
-- This script lists the number of records with the same score in second_table
-- Task 15: Number by score

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
