class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for item in range(len(nums) + 1):
            if item not in nums:
                return item
    