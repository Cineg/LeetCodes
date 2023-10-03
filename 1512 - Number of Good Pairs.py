class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        used_items: dict = {}
        result: int = 0

        for num in nums:
            if num in used_items:
                result += used_items[num]
                used_items[num] += 1 
            else:
                used_items[num] = 1 

        return result