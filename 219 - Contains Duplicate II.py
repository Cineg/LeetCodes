class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen: dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] in seen and abs(i - seen[nums[i]]) <= k:
                return True

            seen[nums[i]] = i
        return False
