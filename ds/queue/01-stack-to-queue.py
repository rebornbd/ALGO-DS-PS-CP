"""
implements queue using stack
"""

# insert costly | enQueue costly
class Queue1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
    
    def deQueue(self):
        if len(self.s1) > 0:
            return self.s1.pop()
        return -1


# deQueue costly
class Queue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):
        self.s1.append(x)
    
    def deQueue(self):
        if len(self.s1) > 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
            
            d = self.s2.pop()
            while len(self.s2) > 0:
                self.s1.append(self.s2.pop())
            return d
        return -1


q = Queue2()

for i in range(1, 10):
    q.enQueue(i*10)

for i in range(1, 10):
    q.enQueue(i+10)

for i in range(1, 20):
    d = q.deQueue()
    print(d)
