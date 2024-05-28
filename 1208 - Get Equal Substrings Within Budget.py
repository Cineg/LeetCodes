from collections import deque


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        prices: list[int] = []
        for i in range(len(s)):
            prices.append(abs(ord(s[i]) - ord(t[i])))

        current_cost: int = maxCost
        dq = deque([])
        maxSize: int = 0

        i: int = 0
        while i < len(prices):
            cost: int = prices[i]
            if cost <= current_cost:
                current_cost -= cost
                dq.append(cost)

                maxSize = max(len(dq), maxSize)
                i += 1

            elif cost > current_cost and len(dq) > 0:
                current_cost += dq.popleft()
                if current_cost > maxCost:
                    current_cost = maxCost

            else:
                i += 1

        return maxSize


def main() -> None:
    sol = Solution()
    s: str = "abcd"
    t: str = "acde"
    maxCost: int = 0

    res: int = sol.equalSubstring(s, t, maxCost)
    print(res)


if __name__ == "__main__":
    main()
