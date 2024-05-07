class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None
        self.prev: Node | None = None


class Deque:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def peekright(self) -> None | int:
        return self.tail.val if self.tail else None

    def peekleft(self) -> None | int:
        return self.head.val if self.head else None

    def popleft(self) -> None | int:
        if not self.head:
            return None

        val: int = self.head.val
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None
        else:
            head: Node | None = self.head.next
            self.head.next = None
            if head:
                head.prev = None
                self.head = head

        return val

    def popright(self) -> None | int:
        if not self.tail:
            return None

        val: int = self.tail.val
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None

        else:
            tail: Node | None = self.tail.prev
            self.tail.prev = None
            if tail:
                tail.next = None
                self.tail = tail

        return val

    def push(self, val: int) -> None:
        self.length += 1
        if self.length == 1:
            self.head = self.tail = Node(val)
            return

        if not self.tail:
            return

        node = Node(val)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res: list[int] = []
        dq = Deque()

        l: int = 0
        r: int = 0

        while r < len(nums):
            while dq.length > 0 and nums[dq.peekright()] < nums[r]:
                dq.popright()
            dq.push(r)

            if l > dq.peekleft():
                dq.popleft()

            if r + 1 >= k:
                res.append(nums[dq.peekleft()])
                l += 1

            r += 1

        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [1, 3, -1, -3, 5, 3, 6, 7]
    k: int = 3

    res: list[int] = sol.maxSlidingWindow(nums, k)
    print(res)


if __name__ == "__main__":
    main()
