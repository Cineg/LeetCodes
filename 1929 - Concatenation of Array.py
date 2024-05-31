class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        l = len(nums)
        for i in range(l):
            nums.append(nums[i])

        return nums
