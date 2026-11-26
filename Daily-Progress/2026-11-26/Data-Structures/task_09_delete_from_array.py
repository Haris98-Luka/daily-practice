# Daily Practice Task 9
# Date: 2026-11-26
# Category: Data Structures
#
# Task: Delete an element from an array.
# Approach: Shift elements left over the deleted position, then drop the last slot.

arr = [10, 20, 30, 40, 50]
position = 1

for i in range(position, len(arr) - 1):
    arr[i] = arr[i + 1]
arr.pop()

print("After delete:", arr)
