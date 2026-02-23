-- 10-top_score.sql
-- This script lists all records of second_table ordered by score (top first)
-- Task 10: List by best

SELECT score, name FROM second_table ORDER BY score DESC;
