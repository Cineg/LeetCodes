from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


class MinHeap:
    def __init__(self) -> None:
        self.length: int = 0
        self.items: list[int] = []

    def insert(self, value: int) -> None:
        self.length += 1
        self.items.append(value)
        self._bubble_up(self.length - 1)

    def pop(self) -> int | None:
        if self.length == 0:
            return

        if self.length == 1:
            self.length -= 1
            return self.items.pop()

        val: int = self.items[0]
        self.items[0] = self.items[self.length - 1]
        self.items.pop()
        self.length -= 1
        self._bubble_down(0)

        return val

    def _bubble_up(self, index: int) -> None:
        p: int = self._get_parent_index(index)
        if p < 0:
            return

        if self.items[p] <= self.items[index]:
            return

        self.items[p], self.items[index] = self.items[index], self.items[p]
        self._bubble_up(p)

    def _bubble_down(self, index: int) -> None:
        c: int | None = self._get_child_index(index)
        if not c:
            return

        if self.items[c] >= self.items[index]:
            return

        self.items[c], self.items[index] = self.items[index], self.items[c]
        self._bubble_down(c)

    def _get_child_index(self, index: int) -> int | None:
        l, r = self._get_children_indexes(index)
        if l >= self.length:
            return None
        if r >= self.length:
            return l

        if self.items[l] <= self.items[r]:
            return l

        return r

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _get_children_indexes(self, index: int) -> tuple[int, int]:
        l: int = (index * 2) + 1
        r: int = (index * 2) + 2
        return l, r


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return

        heap = MinHeap()
        for head in lists:
            while head:
                heap.insert(head.val)
                head: ListNode | None = head.next

        if heap.length == 0:
            return

        node = ListNode(0)
        head = node

        while heap.length > 0:
            val: int | None = heap.pop()
            if val != None:
                node.next = ListNode(val)
                node = node.next

        return head.next


def main():
    sol = Solution()

    l1 = ListNode(0, ListNode(2, ListNode(5)))

    node = sol.mergeKLists([l1])

    print(node)


if __name__ == "__main__":
    main()
