class MyCircularQueue:

    def __init__(self, k: int) -> None:
        self.queue: list[int] = [0] * k
        self.items_queued: int = 0
        self.capacity: int = k
        self.rear: int = -1

    def enQueue(self, value: int) -> bool:
        if self.items_queued + 1 > len(self.queue):
            return False

        self.items_queued += 1 
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.items_queued <= 0:
            return False
        
        self.items_queued -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): 
            return -1
        
        front: int = (self.rear - self.items_queued + 1) % self.capacity
        return self.queue[front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.items_queued == 0

    def isFull(self) -> bool:
        return self.items_queued == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()