# Daily Practice Task 8
# Date: 2026-11-27
# Category: Python
#
# Task: Write a program to find the largest number in a list.
# Approach: Keep track of the biggest value while looping.

numbers = [14, 92, 37, 58, 3]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)
