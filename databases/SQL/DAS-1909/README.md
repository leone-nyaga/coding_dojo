# Diploma in Applied Statistics Database

This repository contains SQL scripts for creating tables related to a Diploma in Applied Statistics program. The database is named `DAS_1909`.

## Tables

### 1. Students

- Table Name: `students`
- Columns:
  - `admission_number` (Primary Key)
  - `first_name`
  - `last_name`
  - `email`
  - `phone_number`
  - `date_of_birth`
  - `enrollment_date`

### 2. Academic Records

- Table Name: `academic_records`
- Columns:
  - `record_id` (Primary Key)
  - `admission_number` (Foreign Key referencing `students`)
  - `course_id` (Foreign Key referencing `courses`)
  - `semester_id` (Foreign Key referencing `semesters`)
  - `grade`
  - `enrollment_date`

### 3. Classrooms

- Table Name: `classrooms`
- Columns:
  - `room_id` (Primary Key)
  - `room_number`
  - `capacity`

## Usage

1. **Create Database:**
   - Execute the SQL command to create the `DAS_1909` database.

2. **Create Tables:**
   - Execute the SQL commands to create the `students`, `academic_records`, and `classrooms` tables.

3. **Explore Relationships:**
   - Utilize foreign keys to establish relationships between tables. Refer to the table definitions for details.


