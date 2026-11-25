# Daily Practice Task 2
# Date: 2026-11-25
# Category: Python
#
# Task: Write a program to calculate factorial.
# Approach: Multiply numbers from 1 to n.

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print("5! =", factorial(5))
print("10! =", factorial(10))
