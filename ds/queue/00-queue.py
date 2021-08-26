
class MyQueue:
    def __init__(self):
        self.queue = []
        self.top = -1
        self.max = 100
    
    def push(self, x):
        if not self.isFull():
            self.top += 1
            self.queue.append(x)
        else:
            print("QUEUE IS FULL")
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.queue.pop(0)
        else:
            print("QUEUE IS EMPTY, DON'T POP")
            return None
    
    def size(self):
        return self.top + 1
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def isFull(self):
        if self.top == self.max - 1:
            return True
        return False
    
    def display(self):
        for i in range(0, len(self.queue)):
            print(f"{self.queue[i]}", end=' ')

# ====================
'''
q = MyQueue()

q.push(1)
q.push(10)

print(q.pop())
print(q.pop())
print(q.pop())
'''
# ====================

from collections import deque

# Initializing a queue
q = deque()

# enQueue | insert
for i in range(0, 5):
    q.append(100+i)

# deQueue | pop
for i in range(0, 10):
    if len(q) > 0:
        q.popleft()


# ======== queue =============
from queue import Queue

q = Queue()

# set queue size
q.maxsize = 8

# enQueue | insert
for i in range(0, 10):
    if not q.full():
        q.put(10+i)
    else:
        print("QUEUE IS FULL")
        break

# deQueue | pop
for i in range(0, 10):
    if not q.empty():
        d = q.get()
        print(d)
    else:
        print("QUEUE IS EMPTY, DON'T POP")
        break
# =====================================
