# Daily Practice Task 13
# Date: 2026-11-25
# Category: Data Structures
#
# Task: Create and display an array.
# Approach: Create a list, then print every element with its index.

arr = [10, 20, 30, 40, 50]

print("Array:", arr)
for index, value in enumerate(arr):
    print(f"arr[{index}] = {value}")
print("Length:", len(arr))
