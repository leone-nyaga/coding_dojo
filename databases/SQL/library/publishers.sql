-- query to create table Publishers

CREATE TABLE IF NOT EXISTS Publishers (
	publisher_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	country VARCHAR(100)
);
