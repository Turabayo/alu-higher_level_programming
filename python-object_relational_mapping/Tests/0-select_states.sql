-- create states table in hbtn_0e_0_usa with some data
IF NOT EXISTS hbtn_0e_0_usa;
a;

CREATE TABLE IF NOT EXISTS states(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id)
);

INSERT INTO states (name) VALUES ("Texas"), ("Ottawa"), ("Toronto"), ("Washington");