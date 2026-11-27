# Daily Practice Task 14
# Date: 2026-11-27
# Category: Python
#
# Task: Write a program to count vowels in a string.
# Approach: Check every character against the set of vowels.

text = "Daily practice makes perfect"
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Vowels:", count)
