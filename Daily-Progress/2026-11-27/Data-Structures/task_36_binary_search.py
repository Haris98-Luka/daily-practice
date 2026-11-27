# Daily Practice Task 36
# Date: 2026-11-27
# Category: Data Structures
#
# Task: Implement binary search.
# Approach: Repeatedly halve a sorted array. Time O(log n).

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = [1, 3, 5, 7, 9, 11, 13]
print("Index of 7:", binary_search(data, 7))
print("Index of 4:", binary_search(data, 4))
