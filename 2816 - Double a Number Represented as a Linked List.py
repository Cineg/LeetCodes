from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes: list[ListNode] = []
        node: ListNode | None = head
        while node:
            nodes.append(node)
            node = node.next

        carry: int = 0
        for node in nodes[::-1]:
            node.val *= 2

            if node.val >= 10:
                temp_carry = 1
            else:
                temp_carry = 0

            node.val %= 10
            node.val += carry

            carry = temp_carry

        if carry == 1:
            temp: ListNode | None = ListNode(1)
            temp.next = head
        else:
            temp = head

        return temp
