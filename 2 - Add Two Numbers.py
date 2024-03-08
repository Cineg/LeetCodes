# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1s: str = ""
        l2s: str = ""

        while l1:
            l1s = str(l1.val) + l1s
            l1 = l1.next

        while l2:
            l2s = str(l2.val) + l2s
            l2 = l2.next

        result: int = int(l1s) + int(l2s)

        dummy: ListNode = ListNode(0)
        result_node: ListNode = dummy

        for item in str(result)[::-1]:
            node = ListNode(int(item))
            result_node.next = node
            result_node = result_node.next

        return dummy.next
