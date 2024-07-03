import math


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) < 4:
            return 0

        min_diff: float = math.inf
        nums.sort()

        for i in range(4):
            min_diff = min(min_diff, nums[-4 + i] - nums[i])

        return int(min_diff)
