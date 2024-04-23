class Node:
    def __init__(self, val: int, min: int | None) -> None:
        self.val: int = val
        self.prev_min: int | None = min
        self.next: Node | None = None


class MinStack:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node | None = None
        self.min: int | None = None

    def push(self, val: int) -> None:
        self.length += 1
        if self.length == 1:
            self.head = Node(val, self.min)
            self.min = val
            return

        node = Node(val, self.min)
        node.next = self.head
        self.head = node

        if self.min != None:
            self.min = min(val, self.min)

    def pop(self) -> None:
        if not self.head:
            return

        self.length -= 1
        self.min = self.head.prev_min
        next_node: Node | None = self.head.next
        self.head = next_node

    def top(self) -> int:
        if self.head:
            return self.head.val

        return -1

    def getMin(self) -> int:
        return self.min if self.min != None else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def main():
    obj = MinStack()
    obj.push(2)
    obj.push(0)
    obj.push(3)
    obj.push(0)

    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())


if __name__ == "__main__":
    main()
