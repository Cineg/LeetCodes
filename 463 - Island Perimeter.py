from collections import deque


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        start: tuple[int, int] = self.getStartingPoint(grid)
        if start == (-1, -1):
            return 0

        perimeter: int = 0
        q: list[tuple[int, int]] = [start]
        deque(q)

        seen: set = set()

        while q:
            row, col = q.pop()

            if (row, col) in seen:
                continue

            seen.add((row, col))

            for dir in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                r: int = row + dir[0]
                c: int = col + dir[1]

                # if (r, c) in seen:
                #     continue

                if r < 0 or c < 0:
                    perimeter += 1
                    continue

                if r >= len(grid) or c >= len(grid[0]):
                    perimeter += 1
                    continue

                if grid[r][c] == 0:
                    perimeter += 1
                    continue

                q.append((r, c))

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
