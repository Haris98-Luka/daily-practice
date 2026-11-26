# Daily Practice Task 47
# Date: 2026-11-26
# Category: Python
#
# Task: Write a program to remove duplicates from a list.
# Approach: Keep an item only the first time it is seen (order preserved).

items = [1, 3, 3, 2, 1, 5, 2, 4]
seen = set()
unique = []
for x in items:
    if x not in seen:
        seen.add(x)
        unique.append(x)
print("Without duplicates:", unique)
