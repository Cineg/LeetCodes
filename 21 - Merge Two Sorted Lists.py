from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = ListNode(0)
        node: ListNode = head

        while list1 != None or list2 != None:
            if list1 and list2:
                if list1.val <= list2.val:
                    node.next = list1
                    node = node.next

                    list1 = list1.next
                else:
                    node.next = list2
                    node = node.next

                    list2 = list2.next

            if list1 and list2 == None:
                node.next = list1
                node = node.next
                list1 = list1.next

            if list2 and list1 == None:
                node.next = list2
                node = node.next
                list2 = list2.next

        return head.next


def main():
    sol = Solution()
    sol.mergeTwoLists(None, ListNode(0))


if __name__ == "__main__":
    main()
