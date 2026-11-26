# Daily Practice Task 21
# Date: 2026-11-26
# Category: Python
#
# Task: Write a program to print FizzBuzz from 1 to 20.
# Approach: Check divisibility by 15 first, then 3, then 5.

for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
