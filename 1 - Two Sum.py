class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left: int = 0
        while left < len(nums):
            right: int = left + 1
            while right < len(nums):
                if nums[left] + nums[right] == target:
                    return [left, right]

                right += 1
            left += 1
