from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, val: T) -> None:
        self.val: T = val
        self.next: Node | None = None


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node | None = None

    def push(self, val: T) -> None:
        self.length += 1
        if self.length == 1:
            self.head = Node(val)
            return

        node: Node = Node(val)
        node.next = self.head
        self.head = node

    def pop(self) -> T | None:
        if self.length == 0 or not self.head:
            return None

        self.length -= 1
        val: T = self.head.val
        node: Node | None = self.head.next
        self.head = node

        return val


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack: Stack[tuple[str, int, int]] = Stack()
        res: list[str] = []

        stack.push(("(", n - 1, n))
        while stack.length > 0:
            data: tuple[str, int, int] | None = stack.pop()
            if not data:
                break

            curr, remaining, closed = data

            if remaining == 0:
                while len(curr) < n * 2:
                    curr += ")"

                if curr not in res:
                    res.append(curr)

            else:
                curr_closed: str = curr + ")"
                curr_open: str = curr + "("
                stack.push((curr_open, remaining - 1, closed))

                if closed - 1 < remaining:
                    continue
                stack.push((curr_closed, remaining, closed - 1))

        return res


def main() -> None:
    sol = Solution()
    n = 3

    res: list[str] = sol.generateParenthesis(n)
    print(res)


if __name__ == "__main__":
    main()
