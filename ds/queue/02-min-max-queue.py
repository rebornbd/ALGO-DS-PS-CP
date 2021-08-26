
class MinQueue:
    def __init__(self):
        self.queue = []
        self.minValue = []
    
    def enQueue(self, x):
        if not self.isEmpty():
            mini = self.minValue[-1]
            if (mini > x):
                self.minValue.append(x)
            else: self.minValue.append(mini)
        else: self.minValue.append(x)
        self.queue.append(x)
    
    
    def deQueue(self):
        if len(self.queue) > 0:
            self.minValue.pop()
            return self.queue.pop(0)
        return None
    
    def getMin(self):
        if len(self.queue) > 0:
            return self.minValue[-1]
        return None
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        return True
    
    def display(self):
        for i in range(0, len(self.queue)):
            print(f"{self.queue[i]}", end=' ')


class MaxQueue:
    def __init__(self):
        self.queue = []
        self.maxValue = []
    
    def enQueue(self, x):
        if not self.isEmpty():
            maxi = self.maxValue[-1]
            if (maxi < x):
                self.maxValue.append(x)
            else: self.maxValue.append(maxi)
        else: self.maxValue.append(x)
        self.queue.append(x)
    
    
    def deQueue(self):
        if len(self.queue) > 0:
            self.maxValue.pop()
            return self.queue.pop(0)
        return None
    
    def getMax(self):
        if len(self.queue) > 0:
            return self.maxValue[-1]
        return None
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        return True
    
    def display(self):
        for i in range(0, len(self.queue)):
            print(f"{self.queue[i]}", end=' ')


q = MinQueue()

q.enQueue(-3)
q.enQueue(100)
q.enQueue(10)
q.enQueue(10)

q.deQueue()
q.deQueue()
print(q.getMin())
