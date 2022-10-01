USE cars_app_db;

CREATE TABLE image(
	image_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	image_url VARCHAR(700)
);

CREATE TABLE model_image(
	model_image_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	model_id INTEGER,
	image_id INTEGER,
	FOREIGN KEY (model_id) REFERENCES model(model_id),
	FOREIGN KEY (image_id) REFERENCES image(image_id) 
);

CREATE TABLE version_image(
	version_image_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
	version_id INTEGER,
	image_id INTEGER,
	FOREIGN KEY (version_id) REFERENCES version(version_id),
	FOREIGN KEY (image_id) REFERENCES image(image_id)
);
