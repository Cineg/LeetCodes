class Node:
    def __init__(self, val: tuple[int, int]) -> None:
        self.val: tuple[int, int] = val
        self.next: Node | None = None


class Queue:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def push(self, val: tuple[int, int]) -> None:
        self.length += 1
        if self.length == 1:
            self.head = self.tail = Node(val)
            return

        if self.tail:
            tail: Node = Node(val)
            self.tail.next = tail
            self.tail = tail

    def pop(self) -> tuple[int, int] | None:
        if not self.head:
            return None

        self.length -= 1
        val: tuple[int, int] = self.head.val
        if self.length == 0:
            self.head = self.tail = None
            return val

        head: Node | None = self.head.next
        self.head.next = None
        self.head = head

        return val


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        start: tuple[int, int] = self.getStartingPoint(grid)
        if start == (-1, -1):
            return 0

        perimeter: int = 0
        q: Queue = Queue()
        q.push(start)

        seen: set = set()

        while q.length > 0:
            val: tuple[int, int] | None = q.pop()
            if val == None:
                continue

            row, col = val

            if (row, col) in seen:
                continue

            seen.add((row, col))

            for dir in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                r: int = row + dir[0]
                c: int = col + dir[1]

                if r < 0 or c < 0:
                    perimeter += 1
                    continue

                if r >= len(grid) or c >= len(grid[0]):
                    perimeter += 1
                    continue

                if grid[r][c] == 0:
                    perimeter += 1
                    continue

                q.push((r, c))

        return perimeter

    def getStartingPoint(self, grid: list[list[int]]) -> tuple[int, int]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return i, j

        return -1, -1


def main():
    sol = Solution()
    grid = [[1, 1], [1, 1]]
    res = sol.islandPerimeter(grid)
    print(res)


if __name__ == "__main__":
    main()
