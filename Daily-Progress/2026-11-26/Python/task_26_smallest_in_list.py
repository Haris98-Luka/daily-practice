# Daily Practice Task 26
# Date: 2026-11-26
# Category: Python
#
# Task: Write a program to find the smallest number in a list.
# Approach: Start with the first value and update when a smaller one appears.

numbers = [27, 4, 91, 13, 8]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("Smallest:", smallest)
