class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        res: int = 0

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                res += 1 + nums[i - 1] - nums[i]
                nums[i] = nums[i - 1] + 1

        return res


def main():
    sol = Solution()
    nums: list[int] = [2, 2, 2, 1]
    res: int = sol.minIncrementForUnique(nums)
    print(res)


if __name__ == "__main__":
    main()
