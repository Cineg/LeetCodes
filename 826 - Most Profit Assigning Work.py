import heapq


class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        dp: list[tuple[int, int]] = list(zip(difficulty, profit))
        dp.sort(reverse=True)
        worker.sort(reverse=True)

        res: int = 0
        pq: list[int] = []

        while worker:
            curr: int = worker.pop()

            while dp and curr >= dp[-1][0]:
                _, val = dp.pop()
                heapq.heappush(pq, -val)

            if pq:
                res += -pq[0]

        return res


def main() -> None:
    sol = Solution()
    difficulty: list[int] = [13, 37, 58]
    profit: list[int] = [4, 90, 96]
    worker: list[int] = [34, 73, 45]

    res: int = sol.maxProfitAssignment(difficulty, profit, worker)
    print(res)


if __name__ == "__main__":
    main()
