from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        if len(self.buffer) == 0:
            raise Exception("Queue is empty")

    def size(self):
        return len(self.buffer)