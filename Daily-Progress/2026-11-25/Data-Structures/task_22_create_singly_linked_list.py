# Daily Practice Task 22
# Date: 2026-11-25
# Category: Data Structures
#
# Task: Create a singly linked list.
# Approach: Append new nodes at the tail.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def display(self):
        values, current = [], self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values) + " -> None")


ll = LinkedList()
for v in (5, 10, 15, 20):
    ll.append(v)
ll.display()
