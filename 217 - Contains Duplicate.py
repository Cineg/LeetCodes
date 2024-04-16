class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])
        return False
