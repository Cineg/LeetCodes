from typing import Any


class Node:
    def __init__(self, val: Any) -> None:
        self.val: Any = val
        self.next: Node | None = None


class Stack:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def add(self, val: Any) -> None:
        self.length += 1
        if self.length == 1 and not self.tail:
            self.head = self.tail = Node(val)
            return

        if not self.tail:
            return

        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def pop(self) -> None | Any:
        if not self.head:
            return None

        val: str = self.head.val
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        else:
            new_head: Node | None = self.head.next
            self.head.next = None
            self.head = new_head

        return val


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:

        seen: set = set()
        q: Stack = Stack()
        q.add(([0, 0, 0, 0], 0))

        while q.length > 0:
            data: None | Any = q.pop()
            if not data:
                return -1

            lock, turn = data
            lock_str: str = "".join(str(x) for x in lock)

            if lock_str in seen or lock_str in deadends:
                continue

            if lock_str == target:
                return turn

            seen.add(lock_str)

            for i in range(4):
                add_lock = lock.copy()
                add_lock[i] += 1
                if add_lock[i] > 9:
                    add_lock[i] = 0

                rem_lock = lock.copy()
                rem_lock[i] -= 1
                if rem_lock[i] < 0:
                    rem_lock[i] = 9

                q.add((add_lock, turn + 1))
                q.add((rem_lock, turn + 1))

        return -1


def main():
    sol = Solution()
    deadends: list = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target: str = "8888"

    res = sol.openLock(deadends, target)
    print(res)


if __name__ == "__main__":
    main()
