# Daily Practice Task 38
# Date: 2026-11-27
# Category: Data Structures
#
# Task: Implement queue using an array.
# Approach: FIFO: add at the back, remove from the front.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            raise IndexError("queue is empty")
        return self.items.pop(0)

    def front(self):
        return self.items[0] if self.items else None


q = Queue()
for v in ("A", "B", "C"):
    q.enqueue(v)
print("Front:", q.front())
print("Dequeued:", q.dequeue())
print("Front now:", q.front())
