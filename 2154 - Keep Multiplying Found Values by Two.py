from collections import Counter


class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        items: dict = Counter(nums)
        item: int = original

        while True:
            if item in items:
                item *= 2
            else:
                break

        return item
