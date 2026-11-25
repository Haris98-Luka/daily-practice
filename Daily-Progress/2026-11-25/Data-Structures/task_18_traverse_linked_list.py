# Daily Practice Task 18
# Date: 2026-11-25
# Category: Data Structures
#
# Task: Traverse a linked list.
# Approach: Start at head and follow .next until None.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
