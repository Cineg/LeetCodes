class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res: list[list[int]] = []

        def walk(idx: int, val: int, curr: list[int]) -> None:
            if val == target:
                if curr not in res:
                    res.append(curr.copy())
                return

            if val > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                walk(i + 1, val + candidates[i], curr)
                curr.pop()

        walk(0, 0, [])
        return res


def main():
    sol = Solution()
    candidates: list[int] = [10, 1, 2, 7, 6, 1, 5]
    target: int = 8
    res: list[list[int]] = sol.combinationSum2(candidates, target)

    print(res)


if __name__ == "__main__":
    main()
