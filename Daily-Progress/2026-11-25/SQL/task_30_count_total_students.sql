-- Daily Practice Task 30
-- Date: 2026-11-25
-- Category: SQL
--
-- Task: Count total students.
-- Approach: COUNT(*) counts rows.

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

SELECT COUNT(*) AS total_students FROM Student;
