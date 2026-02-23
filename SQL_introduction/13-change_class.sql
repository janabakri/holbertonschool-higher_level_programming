-- 13-change_class.sql
-- This script removes all records with a score <= 5 from second_table
-- Task 13: Score too low

DELETE FROM second_table WHERE score <= 5;
