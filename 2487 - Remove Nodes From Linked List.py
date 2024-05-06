from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values: list[ListNode] = []

        node = head
        while node:
            values.append(node)
            node = node.next

        right_max: int = 0
        update_node: bool = False
        for i, node in enumerate(values[::-1]):
            if update_node:
                node.next = node.next.next
                update_node = False

            if node.val < right_max:
                update_node = True
                if i == len(values) - 1:
                    head = head.next
                continue

            right_max = max(node.val, right_max)

        return head


def main() -> None:
    sol = Solution()
    ll = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
    res = sol.removeNodes(ll)

    print(res)


if __name__ == "__main__":
    main()
