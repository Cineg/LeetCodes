class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        seen: dict = {}
        for item in nums1:
            if item not in seen:
                seen[item] = ""

        for item in nums2:
            if item in seen:
                return item

        return -1
