# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l_pointer: ListNode = head
        r_pointer: ListNode = head

        try:
            while r_pointer:
                l_pointer = l_pointer.next
                r_pointer = r_pointer.next.next

                if l_pointer == r_pointer:
                    return True

            return False
        except:
            return False
