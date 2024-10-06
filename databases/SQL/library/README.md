Creating a simple library database in MySQL

TABLES:
=======
1. Books

+ book_id (Primary Key, Auto Increment)
+ title
+ author_id (Foreign Key)
+ publisher_id (Foreign Key)
+ published_year
+ genre

2. Authors
+ author_id (Primary Key, Auto Increment)
+ name
+ birth_year
+ country

3. Publishers
+ publisher_id (Primary Key, Auto Increment)
+ name
+ country

4. Borrowers
+ borrower_id (Primary Key, Auto Increment)
+ name
+ membership_date

5. Loans
+ loan_id (Primary Key, Auto Increment)
+ book_id (Foreign Key)
+ borrower_id (Foreign Key)
+ loan_date
+ return_date

