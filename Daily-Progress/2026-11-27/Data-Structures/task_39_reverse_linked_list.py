# Daily Practice Task 39
# Date: 2026-11-27
# Category: Data Structures
#
# Task: Reverse a singly linked list.
# Approach: Re-point each node's next to the previous node. Time O(n), space O(1).

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


def reverse(head):
    previous = None
    while head:
        head.next, previous, head = previous, head, head.next
    return previous


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original:", to_list(head))
print("Reversed:", to_list(reverse(head)))
