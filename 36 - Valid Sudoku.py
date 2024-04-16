class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # rows
        for row in board:
            seen: set = set()
            for char in row:
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        # cols
        for lock in range(len(board[0])):
            seen: set = set()
            i: int = 0
            for i in range(len(board[0])):
                char: str = board[i][lock]
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        # square
        for i in range(3):
            for j in range(3):
                if not self.check_square(board, i * 3, j * 3):
                    return False

        return True

    def check_square(
        self, board: list[list[str]], row_offset: int, col_offset: int
    ) -> bool:

        seen: set = set()
        for i in range(3):
            for j in range(3):
                char: str = board[i + row_offset][j + col_offset]
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        return True


def main():
    sol = Solution()
    grid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    sol.isValidSudoku(grid)


if __name__ == "__main__":
    main()
