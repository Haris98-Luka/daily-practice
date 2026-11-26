# Daily Practice Task 6
# Date: 2026-11-26
# Category: Data Structures
#
# Task: Count nodes in a linked list.
# Approach: Walk the list and increase a counter for each node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(4)
head.next = Node(8)
head.next.next = Node(15)
head.next.next.next = Node(16)

count, current = 0, head
while current:
    count += 1
    current = current.next
print("Number of nodes:", count)
