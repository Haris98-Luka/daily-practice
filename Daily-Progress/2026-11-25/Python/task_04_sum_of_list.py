# Daily Practice Task 4
# Date: 2026-11-25
# Category: Python
#
# Task: Write a program to find the sum of list elements.
# Approach: Add each element to a running total.

numbers = [4, 8, 15, 16, 23, 42]
total = 0
for n in numbers:
    total += n
print("Sum:", total)
