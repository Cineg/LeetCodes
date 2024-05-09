class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort()
        decrease: int = 0

        res: int = 0
        for _ in range(k):
            val: int = happiness.pop()
            val = max(val - decrease, 0)
            res += val
            decrease += 1

        return res
