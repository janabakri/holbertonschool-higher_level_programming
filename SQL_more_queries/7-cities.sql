-- 7-cities.sql
-- Creates database hbtn_0d_usa and table cities with foreign key to states
-- cities: id (PK), state_id (FK to states.id), name
-- If database or table already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
