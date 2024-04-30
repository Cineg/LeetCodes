# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack: list[Optional[ListNode]] = []
        node: Optional[ListNode] = head
        while node != None:
            stack.append(node)
            node = node.next

        rev: ListNode = ListNode(0)
        node = rev
        while stack:
            n: ListNode | None = stack.pop()
            node.next = ListNode(n.val) if n else None
            node = node.next

        return rev.next


def main():
    sol = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res: ListNode | None = sol.reverseList(l)
    print("XD")


if __name__ == "__main__":
    main()
