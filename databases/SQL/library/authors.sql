-- query to create table Authors

CREATE TABLE IF NOT EXISTS Authors (
	author_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	birth_year INT,
	country VARCHAR(100)
);
