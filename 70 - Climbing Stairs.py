class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        temp: int = 0
        steps: int = 1
        previous_steps: int = 1

        for i in range(n-1):
            temp = steps
            steps = steps + previous_steps
            previous_steps = temp

        return steps