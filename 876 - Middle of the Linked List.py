# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left_p: ListNode = head
        right_p: ListNode = head

        while right_p and right_p.next:
            left_p = left_p.next
            right_p = right_p.next.next

        return left_p
