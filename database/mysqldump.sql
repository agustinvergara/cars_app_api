DROP DATABASE IF EXISTS cars_app_db;

CREATE DATABASE cars_app_db;

USE cars_app_db;

CREATE TABLE brands(
	brand_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	brand_name VARCHAR(70)
);

CREATE TABLE segment(
	segment_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	segment_name VARCHAR(70)
);

CREATE TABLE model(
	model_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	brand_id INTEGER,
	segment_id INTEGER,
	model_name VARCHAR(70),
	FOREIGN KEY (segment_id) REFERENCES segment(segment_id),
	FOREIGN KEY (brand_id) REFERENCES brands(brand_id)
);

CREATE TABLE version(
	version_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	model_id INTEGER,
	version_name VARCHAR(80),
	price FLOAT,
	year YEAR DEFAULT 2022,
	power_hp INTEGER DEFAULT 0,
	torque INTEGER DEFAULT 0,
	traction VARCHAR(70) DEFAULT '4x2',
	automatic BOOLEAN DEFAULT 1,
	good_capacity TINYINT DEFAULT 5,
	autonomy TINYINT DEFAULT 3,
	low_gas_use TINYINT DEFAULT 5,
	screen BOOLEAN DEFAULT 0,
	fiability TINYINT DEFAULT 5,
	interior_space VARCHAR(70),
	spacious TINYINT DEFAULT 5,
	interiors VARCHAR(60) DEFAULT 'TELA',
	secure TINYINT DEFAULT 5,
	passengers INTEGER DEFAULT 4,
	is_comfortable TINYINT DEFAULT 5,
	sunroof BOOLEAN DEFAULT 0,
	is_functional TINYINT DEFAULT 5,
	stetic TINYINT DEFAULT 5,
	attractive TINYINT DEFAULT 5,
	rims VARCHAR(70) DEFAULT 'genericos con copa',
	color_hexa VARCHAR(50) DEFAULT 'FFFFFF',
	FOREIGN KEY (model_id) REFERENCES model(model_id)
);

CREATE TABLE car_image(
	car_image_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	version_id INTEGER,
	car_image_1 VARCHAR(700),
	car_image_2 VARCHAR(700),
	car_image_3 VARCHAR(700),
	FOREIGN KEY (version_id) REFERENCES version(version_id)
);
