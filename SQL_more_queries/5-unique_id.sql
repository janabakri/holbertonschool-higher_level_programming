-- 5-unique_id.sql
-- Creates table unique_id with id default 1 and unique constraint
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
