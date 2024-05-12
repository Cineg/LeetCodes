class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n: int = len(grid)

        res: list[list[int]] = []
        for i in range(1, n - 1):
            temp_row: list[int] = []
            for j in range(1, n - 1):

                temp: int = 0
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        temp = max(temp, grid[r][c])

                temp_row.append(temp)
            res.append(temp_row)

        return res
