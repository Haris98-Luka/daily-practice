# Daily Practice Task 5
# Date: 2026-11-25
# Category: Python
#
# Task: Write a program to count words in a sentence.
# Approach: split() breaks the sentence on whitespace.

sentence = "Consistency beats intensity every single time"
words = sentence.split()
print("Word count:", len(words))
