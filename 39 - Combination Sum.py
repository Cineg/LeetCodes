class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []

        def walk(c_idx: int, cur: list[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return

            if c_idx >= len(candidates) or total > target:
                return

            cur.append(candidates[c_idx])
            walk(c_idx, cur, total + candidates[c_idx])

            cur.pop()
            walk(c_idx + 1, cur, total)

        walk(0, [], 0)
        return res


def main() -> None:
    sol = Solution()
    target: int = 7
    candidates: list[int] = [2, 3, 6, 7]

    res: list[list[int]] = sol.combinationSum(candidates, target)
    print(res)


if __name__ == "__main__":
    main()
