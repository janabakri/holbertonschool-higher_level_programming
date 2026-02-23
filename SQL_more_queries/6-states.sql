-- 6-states.sql
-- This script creates database hbtn_0d_usa and table states (with id and name)
-- Task 6: States table

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table if not exists
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
