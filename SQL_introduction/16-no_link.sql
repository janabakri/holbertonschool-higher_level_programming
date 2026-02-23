-- 16-no_link.sql
-- This script lists all records of second_table with a name value
-- Task 16: Say my name

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
