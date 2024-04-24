class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res: list[int] = [0] * len(temperatures)

        # index, temp
        stack: list[tuple[int, int]] = []

        i: int = 0
        while i < len(temperatures):
            while stack and stack[-1][1] < temperatures[i]:
                if stack[-1][1] < temperatures[i]:
                    idx, _ = stack.pop()
                    res[idx] = i - idx
                else:
                    break

            stack.append((i, temperatures[i]))
            i += 1

        return res


def main() -> None:
    sol = Solution()
    temp: list[int] = [73, 74, 75, 71, 69, 72, 76, 73]
    res: list[int] = sol.dailyTemperatures(temp)
    print(res)


if __name__ == "__main__":
    main()
