class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if not cost:
            return 0

        temp: int = 0
        option1: int = cost[0]

        if len(cost) >= 2:
            option2: int = cost[1]

        for i in range(2, len(cost)):
            temp = cost[i] + min(option1, option2)
            option1 = option2
            option2 = temp

        return min(option1, option2)