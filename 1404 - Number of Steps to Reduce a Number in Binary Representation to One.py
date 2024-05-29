class Solution:
    def numSteps(self, s: str) -> int:
        num: int = int(s, 2)
        steps: int = 0
        while num > 1:
            if num % 2 == 1:
                num += 1
                steps += 1

            num //= 2
            steps += 1

        return steps


def main() -> None:
    sol = Solution()
    s: str = "10"
    res: int = sol.numSteps(s)
    print(res)


if __name__ == "__main__":
    main()
