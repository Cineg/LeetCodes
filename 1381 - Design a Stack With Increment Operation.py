class CustomStack:

    def __init__(self, maxSize: int) -> None:
        self.arr: list = []
        self.max_capacity: int = maxSize
        self.capacity: int = 0

    def push(self, x: int) -> None:
        if self.capacity == self.max_capacity:
            return

        self.capacity += 1
        self.arr.append(x)

    def pop(self) -> int:
        if self.capacity == 0:
            return -1

        self.capacity -= 1
        return self.arr.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.capacity)):
            self.arr[i] += val
