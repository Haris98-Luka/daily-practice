-- Daily Practice Task 28
-- Date: 2026-11-27
-- Category: SQL
--
-- Task: Create a Student table.
-- Approach: CREATE TABLE defines columns, types and the primary key.

CREATE TABLE Student (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT,
    marks INTEGER
);

-- Check the table structure
PRAGMA table_info(Student);
