# Daily Practice Task 32
# Date: 2026-11-27
# Category: Data Structures
#
# Task: Implement bubble sort.
# Approach: Repeatedly swap neighbours that are out of order. Time O(n^2).

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
