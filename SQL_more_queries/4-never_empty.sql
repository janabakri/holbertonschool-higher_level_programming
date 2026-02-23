-- 4-never_empty.sql
-- This script creates table id_not_null with id default value 1 and name
-- Task 4: ID can't be null

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
