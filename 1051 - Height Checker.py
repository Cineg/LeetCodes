class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        h_s: list[int] = heights.copy()
        h_s.sort()

        res: int = 0
        for i, _ in enumerate(heights):
            if heights[i] != h_s[i]:
                res += 1

        return res
