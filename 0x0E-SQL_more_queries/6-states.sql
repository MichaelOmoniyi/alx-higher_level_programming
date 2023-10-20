-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to a database
USE hbtn_0d_usa;
-- Creates a table
CREATE TABLE IF NOT EXISTS states(
    `id` INT UNIQUE NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
     PRIMARY KEY(id));
