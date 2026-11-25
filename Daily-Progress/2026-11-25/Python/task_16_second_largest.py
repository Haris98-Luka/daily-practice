# Daily Practice Task 16
# Date: 2026-11-25
# Category: Python
#
# Task: Write a program to find the second largest number in a list.
# Approach: Remove duplicates, sort, and take the second last item.

numbers = [12, 35, 1, 10, 34, 1, 35]
unique = sorted(set(numbers))
if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("Not enough distinct numbers")
