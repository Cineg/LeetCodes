import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares: list[int] = []
        for i in range(math.ceil(math.sqrt(c)) + 1):
            squares.append(i * i)

        l: int = 0
        r: int = len(squares) - 1
        while l <= r:
            res: int = squares[l] + squares[r]
            if res == c:
                return True

            elif res < c:
                l += 1
            elif res > c:
                r -= 1

        return False


def main() -> None:
    sol = Solution()
    c: int = 2
    res: bool = sol.judgeSquareSum(c)
    print(res)


if __name__ == "__main__":
    main()
