from typing import Any


class Node:
    def __init__(self, val) -> None:
        self.value: Any = val
        self.next: Node | None = None
        self.prev: Node | None = None


class Queue:
    def __init__(self) -> None:
        self.length = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, val) -> None:
        self.length += 1

        if self.length == 1:
            self.head = self.tail = Node(val)
            return

        if not self.tail:
            return

        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def pop(self) -> None:
        if not self.head:
            return None

        self.length -= 1
        val = self.head.value

        if self.length == 0:
            self.head = self.tail = None
        else:
            next_head = self.head.next
            self.head.next = None
            self.head = next_head

        return val


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        island_count: int = 0
        seen: set = set()

        for ridx, row in enumerate(grid):
            for cidx, val in enumerate(row):
                if val == "1":
                    island_count += 1
                    self.update_adjacent(ridx, cidx, grid, seen)

        return island_count

    def update_adjacent(
        self, ridx: int, cidx: int, grid: list[list[str]], seen: set
    ) -> None:
        q = Queue()
        q.append((ridx, cidx))

        while q.length > 0:
            data: None | Any = q.pop()
            if data == None:
                return

            r, c = data
            if (r, c) in seen:
                continue

            # update to 0
            grid[r][c] = "0"
            seen.add((r, c))
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_r: int = r + x
                new_c: int = y + c

                if new_r < 0 or new_c < 0:
                    continue
                if new_r >= len(grid) or new_c >= len(grid[0]):
                    continue

                if grid[new_r][new_c] == "0":
                    continue

                q.append((new_r, new_c))


def main():
    sol = Solution()

    input = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    res = sol.numIslands(input)
    print(res)


if __name__ == "__main__":
    main()
