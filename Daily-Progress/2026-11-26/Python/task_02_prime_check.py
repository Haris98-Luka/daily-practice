# Daily Practice Task 2
# Date: 2026-11-26
# Category: Python
#
# Task: Write a program to check whether a number is prime.
# Approach: A prime has no divisor between 2 and sqrt(n).

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for number in (2, 17, 18, 29, 100):
    print(number, "is prime" if is_prime(number) else "is not prime")
