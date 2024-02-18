class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()

        nums_sum: int = 0
        index: int = 0

        while index < len(nums):
            if (index + 1) % 2 == 0:
                nums_sum += min(nums[index], nums[index - 1])
            index += 1

        return nums_sum
