class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen: dict = {(0, 0): 1}
        queue: list = [(0, 0)]
        count: int = 0
        while queue:
            row, col = queue.pop(0)

            if row == m - 1 and col == n - 1:
                return seen[(row, col)]

            for dir in [(0, 1), (1, 0)]:
                new_row: int = row + dir[0]
                new_col: int = col + dir[1]

                if not self.is_out_of_bounds(new_row, new_col, m, n):
                    continue

                if (new_row, new_col) in seen:
                    seen[(new_row, new_col)] += seen[row, col]
                else:
                    seen[(new_row, new_col)] = seen[row, col]
                    queue.append((new_row, new_col))

    def is_out_of_bounds(self, row, col, bound_row, bound_col) -> bool:
        if row >= bound_row or col >= bound_col:
            return False

        return True


def main():
    sol = Solution()
    res = sol.uniquePaths(3, 7)
    print(res)


if __name__ == "__main__":
    main()
