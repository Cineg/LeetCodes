class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        r: int = 0
        while r < len(matrix):
            if matrix[r][0] <= target <= matrix[r][-1]:
                break

            r += 1

        if r >= len(matrix):
            return False

        pivot: int = len(matrix[r]) // 2

        def walk(self, row: list[int], lo: int, hi: int) -> bool:
            pivot: int = lo + (hi - lo) // 2
            if lo >= hi:
                return False

            if target == row[pivot]:
                return True

            if target < row[pivot]:
                return walk(self, row, lo, pivot)

            else:
                return walk(self, row, pivot + 1, hi)

        return walk(self, matrix[r], 0, pivot) or walk(
            self, matrix[r], pivot, len(matrix[r])
        )


def main() -> None:
    sol = Solution()
    matrix: list[list[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target: int = 13

    res: bool = sol.searchMatrix(matrix, target)
    print(res)


if __name__ == "__main__":
    main()
