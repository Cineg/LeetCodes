from collections import Counter


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnt: Counter = Counter(nums1)

        result: list[int] = []
        for item in cnt:
            if item in nums2:
                result.append(item)

        return result
