import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        n: int = len(capital)
        projects: list[tuple[int, int]] = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()

        i: int = 0
        pq: list[int] = []
        while k > 0:
            while i < n and projects[i][0] <= w:
                heapq.heappush(pq, -projects[i][1])
                i += 1
            if not pq:
                break
            w -= heapq.heappop(pq)
            k -= 1

        return w


def main():
    sol = Solution()
    k = 1
    w = 0
    profits: list[int] = [1, 2, 3]
    capital: list[int] = [1, 1, 1]

    res: int = sol.findMaximizedCapital(k, w, profits, capital)
    print(res)


if __name__ == "__main__":
    main()
