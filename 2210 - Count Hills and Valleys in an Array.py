class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        result: int = 0
        for i in range(1, len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                result += 1
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                result += 1
        
        return result
