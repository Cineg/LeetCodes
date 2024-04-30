# Definition for singly-linked list.
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        q = []
        node = head.next
        while node:
            q.append(node)
            node = node.next

        deq = deque(q)
        node = head
        while deq:
            next_node = deq.pop()
            if not next_node:
                break

            node.next = next_node
            next_node.next = None
            node = next_node

            next_node = deq.popleft()
            if not next_node:
                break

            node.next = next_node
            next_node.next = None
            node = next_node
