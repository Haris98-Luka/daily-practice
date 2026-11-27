# Daily Practice Task 25
# Date: 2026-11-27
# Category: Data Structures
#
# Task: Implement linear search.
# Approach: Check each element one by one. Time O(n).

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


data = [7, 3, 9, 1, 5]
print("Index of 9:", linear_search(data, 9))
print("Index of 4:", linear_search(data, 4))
