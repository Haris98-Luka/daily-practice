-- Daily Practice Task 38
-- Date: 2026-11-25
-- Category: SQL
--
-- Task: Insert five student records.
-- Approach: One INSERT with several value rows.

CREATE TABLE Student (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT,
    marks INTEGER
);

INSERT INTO Student (id, name, class, marks) VALUES
    (1, 'Ali', '10-A', 85),
    (2, 'Sara', '10-A', 92),
    (3, 'Usman', '10-B', 74),
    (4, 'Ayesha', '10-B', 88),
    (5, 'Bilal', '10-A', 67);

-- Verify
SELECT COUNT(*) AS total_rows FROM Student;
