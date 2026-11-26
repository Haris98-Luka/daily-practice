-- Daily Practice Task 13
-- Date: 2026-11-26
-- Category: SQL
--
-- Task: Delete a student record.
-- Approach: DELETE FROM ... WHERE removes matching rows only.

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

DELETE FROM Student WHERE id = 3;

SELECT * FROM Student;
