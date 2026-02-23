-- 3-force_name.sql
-- This script creates table force_name with id and name (name cannot be null)
-- Task 3: Always a name

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
