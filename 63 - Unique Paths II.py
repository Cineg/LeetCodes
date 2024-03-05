class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        grid: list[list[int]] = self.create_empty_grid(
            len(obstacleGrid), len(obstacleGrid[0])
        )

        if obstacleGrid[0][0] != 1:
            grid[0][0] = 1

        visited: set[tuple[int, int]] = {(-1, -1)}
        queue: list[tuple[int, int]] = [(0, 0)]

        while queue:
            row, col = queue.pop(0)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for dir in [(1, 0), (0, 1)]:
                new_row: int = row + dir[0]
                new_col: int = col + dir[1]

                if new_row >= len(obstacleGrid) or new_col >= len(obstacleGrid[0]):
                    continue

                if obstacleGrid[new_row][new_col] != 1:
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] += grid[row][col]

        return grid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

    def create_empty_grid(self, rows: int, cols: int) -> list[list[int]]:
        grid: list[list[int]] = []
        for row in range(rows):
            grid_row: list[int] = []
            for col in range(cols):
                grid_row.append(0)

            grid.append(grid_row)

        return grid


def main():
    sol: Solution = Solution()
    grid: list[list[int]] = [[0, 1], [0, 0]]

    print(sol.uniquePathsWithObstacles(grid))


if __name__ == "__main__":
    main()
