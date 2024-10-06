-- query to create table Books
-- references to tables Authors and Publishers

CREATE TABLE IF NOT EXISTS Books (
	book_id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	author_id INT,
	publisher_id INT,
	published_year INT,
	genre VARCHAR(100),
	FOREIGN KEY (author_id) REFERENCES Authors(author_id),
	FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
);
