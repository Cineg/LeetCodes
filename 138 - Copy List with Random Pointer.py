# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val: int = x
        self.next: Node | None = next
        self.random: Node | None = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        mapping: dict[Node, dict[str, Node | None]] = {}

        node: Node | None = head
        while node:
            mapping[node] = {
                "new": Node(node.val),
                "next": node.next,
                "random": node.random,
            }
            node = node.next

        node = head
        dummy: Node | None = Node(0)
        while node:
            dummy.next = mapping[node]["new"]
            dummy = dummy.next

            # get random
            random = mapping[node]["random"]
            random = mapping[random]["new"]

            dummy.random = random
