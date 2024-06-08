class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        nums.sort()

        def walk(arr: list[int], idx: int) -> None:
            if idx == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[idx])
            walk(arr, idx + 1)
            arr.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            walk(arr, idx + 1)

        walk([], 0)

        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [4, 4, 4, 1, 4]
    res: list[list[int]] = sol.subsetsWithDup(nums)
    print(res)


if __name__ == "__main__":
    main()
