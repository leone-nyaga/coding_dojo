-- querry to create Table Borrowers

CREATE TABLE IF NOT EXISTS Borrowers (
	borrower_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	membership_date DATE
);
