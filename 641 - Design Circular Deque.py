class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None
        self.prev: Node | None = None


class MyCircularDeque:

    def __init__(self, k: int) -> None:
        self.capacity: int = k
        self.current_capacity: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def insertFront(self, value: int) -> bool:
        if self.current_capacity == self.capacity:
            return False

        if self.current_capacity == 0:
            self.head = self.tail = Node(value)
        else:
            temp: Node = self.head
            node = Node(value)
            node.next = temp
            temp.prev = node
            self.head = node

        self.current_capacity += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.current_capacity == self.capacity:
            return False

        if self.current_capacity == 0:
            self.head = self.tail = Node(value)

        else:
            temp: Node = self.tail
            node = Node(value)
            node.prev = temp
            temp.next = node
            self.tail = node

        self.current_capacity += 1
        return True

    def deleteFront(self) -> bool:
        if not self.head:
            return False

        self.current_capacity -= 1
        if self.current_capacity == 0:
            self.head = self.tail = None
            return True

        node: Node = self.head.next
        node.prev = None
        self.head = node
        return True

    def deleteLast(self) -> bool:
        if not self.tail:
            return False

        self.current_capacity -= 1
        if self.current_capacity == 0:
            self.head = self.tail = None
            return True

        node: Node = self.tail.prev
        node.next = None
        self.tail = node
        return True

    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if not self.tail:
            return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        return True if self.current_capacity == 0 else False

    def isFull(self) -> bool:
        return True if self.current_capacity == self.capacity else False


def main() -> None:
    sol = MyCircularDeque(3)
    print(sol.insertLast(1))
    print(sol.insertLast(2))
    print(sol.insertFront(3))
    print(sol.insertFront(4))
    print(sol.getRear())
    print(sol.isFull())
    print(sol.deleteLast())
    print(sol.insertFront(4))
    print(sol.getFront())


if __name__ == "__main__":
    main()
