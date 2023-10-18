from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        cnt: dict = Counter(nums)
        arr: list = []
        for item in cnt:
            if len(arr) == 2: break
            if cnt[item] == 1:
                arr.append(item)
        
        return arr