# Daily Practice Task 27
# Date: 2026-11-27
# Category: Python
#
# Task: Write a program to check whether a string is a palindrome.
# Approach: Compare the cleaned string with its reverse.

def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


for word in ("level", "Was it a car or a cat I saw", "python"):
    print(repr(word), "->", is_palindrome(word))
