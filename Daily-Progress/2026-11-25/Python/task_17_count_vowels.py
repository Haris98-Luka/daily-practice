# Daily Practice Task 17
# Date: 2026-11-25
# Category: Python
#
# Task: Write a program to count vowels in a string.
# Approach: Check every character against the set of vowels.

text = "Daily practice makes perfect"
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Vowels:", count)
