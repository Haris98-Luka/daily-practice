-- Daily Practice Task 40
-- Date: 2026-11-26
-- Category: SQL
--
-- Task: Find students whose name starts with 'A'.
-- Approach: LIKE 'A%' matches any text beginning with A.

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

SELECT name FROM Student WHERE name LIKE 'A%';
