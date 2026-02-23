-- 2-create_read_user.sql
-- Creates database hbtn_0d_2 and user user_0d_2 with SELECT privilege
-- Password: user_0d_2_pwd
-- If database or user already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
