-- MySQL Schema
CREATE DATABASE IF NOT EXISTS logger;
USE logger;

CREATE TABLE IF NOT EXISTS Access (
	AccessCount INTEGER PRIMARY KEY AUTO_INCREMENT,
	Time timestamp DEFAULT CURRENT_TIMESTAMP,
	IP NVARCHAR(128),
	asOrganization NVARCHAR(128),
	country NVARCHAR(128),
	region NVARCHAR(128),
	postalCode NVARCHAR(128),
	city NVARCHAR(128),
	latitude REAL,
	longitude REAL,
	timezone NVARCHAR(128),
    url NVARCHAR(512),
	useragent NVARCHAR(1024)
	);
