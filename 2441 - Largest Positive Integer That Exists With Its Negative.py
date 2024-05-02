class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        largest: int = -1
        d: dict = {}
        for i in nums:
            n: int = abs(i)
            if n in d:
                d[n].add(i)
            else:
                d[n] = set()
                d[n].add(i)

        for i in d:
            largest = max(largest, i) if len(d[i]) > 1 else largest

        return largest
