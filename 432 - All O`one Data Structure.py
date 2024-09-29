class Node:
    def __init__(self, freq: int) -> None:
        self.freq: int = freq
        self.keys: set[str] = set()
        self.next: Node | None = None
        self.prev: Node | None = None


class AllOne:

    def __init__(self):
        self.head: Node = Node(0)
        self.tail: Node = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.node_dict: dict[str, Node] = {}

    def _insert_node(self, prev_node: Node, freq: int) -> Node:
        n = Node(freq)
        n.prev = prev_node
        n.next = prev_node.next

        prev_node.next.prev = n
        prev_node.next = n

        return n

    def _try_remove_node(self, node: Node) -> None:
        if node.keys:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        return

    def inc(self, key: str) -> None:
        if key not in self.node_dict:
            node: Node = self.head.next
            if node == self.tail or node.freq != 1:
                node = self._insert_node(self.head, 1)

            node.keys.add(key)
            self.node_dict[key] = node
            return

        node = self.node_dict[key]
        node.keys.remove(key)

        if node.next == self.tail or node.next.freq != node.freq + 1:
            next_node: Node = self._insert_node(node, node.freq + 1)
        else:
            next_node = node.next

        next_node.keys.add(key)
        self.node_dict[key] = next_node

        self._try_remove_node(node)

    def dec(self, key: str) -> None:
        if key not in self.node_dict:
            return

        node: Node = self.node_dict[key]
        node.keys.remove(key)

        if node.freq == 1:
            del self.node_dict[key]
        else:
            prev_node: Node = node.prev
            if node.prev == self.head or node.prev.freq != node.freq - 1:
                prev_node = self._insert_node(node.prev, node.freq - 1)

            prev_node.keys.add(key)
            self.node_dict[key] = prev_node

        self._try_remove_node(node)

    def getMaxKey(self) -> str:
        for i in self.tail.prev.keys:
            return i
        return ""

    def getMinKey(self) -> str:
        for i in self.head.next.keys:
            return i
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


def main() -> None:
    sol = AllOne()
    sol.inc("a")
    sol.inc("b")
    sol.inc("b")
    sol.inc("b")
    sol.inc("b")
    sol.dec("b")
    sol.dec("b")
    sol.getMaxKey()
    sol.getMinKey()


if __name__ == "__main__":
    main()
