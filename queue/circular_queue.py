class CircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.capacity = k
        self.headIndex = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity