# Daily Practice Task 15
# Date: 2026-11-26
# Category: Data Structures
#
# Task: Implement stack using an array.
# Approach: LIFO: push and pop happen at the end of the list.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise IndexError("stack is empty")
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None


s = Stack()
for v in (10, 20, 30):
    s.push(v)
print("Top:", s.peek())
print("Popped:", s.pop())
print("Top now:", s.peek())
