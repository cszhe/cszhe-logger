-- MySQL Schema
CREATE DATABASE IF NOT EXISTS access;
USE access;

CREATE TABLE IF NOT EXISTS Access (
	AccessCount INTEGER PRIMARY KEY AUTO_INCREMENT,
	Time timestamp DEFAULT CURRENT_TIMESTAMP,
	IP NVARCHAR(128),
	asOrganization NVARCHAR(128),
	country NVARCHAR(64),
	region NVARCHAR(128),
	postalCode NVARCHAR(128),
	city NVARCHAR(64),
	latitude REAL,
	longitude REAL,
	timezone NVARCHAR(128),
    url NVARCHAR(256),
	useragent NVARCHAR(256)
	);
