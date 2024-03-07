class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()

        total: int = 0
        while piles:
            piles.pop(0)
            piles.pop(-1)
            total += piles.pop(-1)

        return total
