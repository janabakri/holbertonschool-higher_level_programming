-- 11-best_score.sql
-- This script lists all records with score >= 10 from second_table
-- Task 11: Select the best

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
