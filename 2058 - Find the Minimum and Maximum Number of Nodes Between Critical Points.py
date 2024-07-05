# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        prev = head
        node = head.next

        idx: int = 1
        criticals: list[int] = []

        while node.next:
            if (prev.val < node.val and node.val > node.next.val) or (
                prev.val > node.val and node.val < node.next.val
            ):
                criticals.append(idx)

            prev = node
            node = node.next
            idx += 1

        if len(criticals) < 2:
            return [-1, -1]
        if len(criticals) == 2:
            dist = abs(criticals[0] - criticals[1])
            return [dist, dist]

        print(criticals)
        i: int = 0
        min_dist: int = criticals[-1]
        while i < len(criticals) - 1:
            min_dist = min(criticals[i + 1] - criticals[i], min_dist)
            i += 1

        return [min_dist, criticals[-1] - criticals[0]]
