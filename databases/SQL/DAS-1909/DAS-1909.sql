-- DAS-1909.sql

CREATE DATABASE IF NOT EXISTS DAS_1909;
USE DAS_1909;

CREATE TABLE students (
    admission_number INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(15),
    date_of_birth DATE,
    enrollment_date DATE
);

CREATE TABLE academic_records (
    record_id INT PRIMARY KEY,
    admission_number INT,
    course_id INT,
    semester_id INT,
    grade VARCHAR(2),
    enrollment_date DATE,
    FOREIGN KEY (admission_number) REFERENCES students(admission_number),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (semester_id) REFERENCES semesters(semester_id)
);

CREATE TABLE classrooms (
    room_id INT PRIMARY KEY,
    room_number VARCHAR(10),
    capacity INT
);
