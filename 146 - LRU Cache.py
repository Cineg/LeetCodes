class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None
        self.prev: Node | None = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.items: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None
        self.nodes: dict[int, Node] = {}
        self.keys: dict[Node, int] = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        if not self.head or not self.tail:
            return -1

        node: Node = self.nodes[key]
        if node == self.head:
            return node.val

        if node == self.tail:
            self.put(key, node.val)
            return node.val

        # move to front
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self._remove_by_key(key)

        self.items += 1
        self._remove_last()

        node: Node = Node(value)
        self.nodes[key] = node
        self.keys[node] = key

        if not self.head:
            self.head = self.tail = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def _remove_last(self) -> None:
        if self.capacity >= self.items:
            return

        self.items = self.capacity

        if not self.tail:
            return
        
        if self.capacity == 1:
            key = self.keys[self.tail]
            self.nodes.pop(key)
            self.keys.pop(self.tail)
            
            self.head = self.tail = None
            return

        new_tail: Node | None = self.tail.prev
        old_tail: Node = self.tail

        self.tail.prev = None
        self.tail.next = None
        self.tail = new_tail

        if self.tail:
            self.tail.next = None
        else:
            self.tail = self.head

        key: int = self.keys[old_tail]

        self.nodes.pop(key)
        self.keys.pop(old_tail)

    def _remove_by_key(self, key: int) -> None:
        if key not in self.nodes:
            return

        node: Node = self.nodes[key]
        self.keys.pop(node)
        self.nodes.pop(key)

        if not self.head or not self.tail:
            return

        self.items -= 1

        if node == self.head:
            self.head = self.head.next
            if not self.head:
                self.head = self.tail = None
            else:
                self.head.prev = None

        elif node == self.tail:
            self.tail = self.tail.prev
            if not self.tail:
                self.head = self.tail = None
            else:
                self.tail.next = None

        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev


def main() -> None:
    cache = LRUCache(1)
    print(cache.get(6))
    print(cache.get(8))
    cache.put(12, 1)
    print(cache.get(2))
    cache.put(15, 11)
    cache.put(5, 2)
    cache.put(1, 15)
    cache.put(4, 2)
    print(cache.get(5))
    cache.put(15, 15)


if __name__ == "__main__":
    main()
