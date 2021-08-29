
class CircularQueue:
    def __init__(self, size = 10):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [None for _ in range(size)]
    
    def enQueue(self, data):
        if self.isFull():
            print(f"QUEUE IS FULL. CAN'T PUSH: {data}")
        
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    
    def deQueue(self):
        if self.isEmpty():
            print("QUEUE IS EMPTY. CAN'T POP DATA!")
        
        else:
            data = self.queue[self.front]
            
            if (self.front == self.rear):
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return data
    
    def isFull(self):
        if ((self.rear + 1) % self.size == self.front):
            return True
        return False
    
    def isEmpty(self):
        if self.front == -1:
            return True
        return False
    
    def display(self):
        if not self.isEmpty():
            print(f"front: {self.front}")
            print(f"rear: {self.rear}")
            
            if (self.rear >= self.front):
                for i in range(self.front, self.rear+1):
                    print(f"{self.queue[i]}", end=" ")
            else:
                for i in range(self.front, self.size):
                    print(f"{self.queue[i]}", end=" ")
                for i in range(0, self.rear+1):
                    print(f"{self.queue[i]}", end=" ")


q = CircularQueue(5)

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)

q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()

# q.deQueue()

# q.enQueue(6)
q.enQueue(7)


q.display()
