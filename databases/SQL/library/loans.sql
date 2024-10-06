-- querry to create Table loans
-- table references table Books and Borrowers

CREATE TABLE IF NOT EXISTS Loans (
	loan_id INT AUTO_INCREMENT PRIMARY KEY,
	book_id INT,
	borrower_id INT,
	loan_date DATE,
	return_date DATE,
	FOREIGN KEY (book_id) REFERENCES Books(book_id),
	FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id)
);
