# Daily Practice Task 18
# Date: 2026-11-26
# Category: Data Structures
#
# Task: Find the middle node of a linked list.
# Approach: Two pointers: slow moves 1 step, fast moves 2. When fast ends, slow is in the middle.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
current = head
for v in (2, 3, 4, 5):
    current.next = Node(v)
    current = current.next

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print("Middle node value:", slow.value)
