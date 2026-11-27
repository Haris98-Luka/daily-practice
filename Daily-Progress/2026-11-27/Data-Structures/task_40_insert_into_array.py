# Daily Practice Task 40
# Date: 2026-11-27
# Category: Data Structures
#
# Task: Insert an element into an array.
# Approach: Shift elements right to make space, then place the value.

arr = [10, 20, 30, 40, 50]
position, value = 2, 99

arr.append(None)  # make room
for i in range(len(arr) - 1, position, -1):
    arr[i] = arr[i - 1]
arr[position] = value

print("After insert:", arr)
