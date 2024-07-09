class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        wait_time: int = 0
        time: int = 1
        for arrival, prep in customers:
            if time < arrival:
                time = arrival
            time = time + prep
            wait_time += time - arrival

        return wait_time / len(customers)


def main() -> None:
    sol = Solution()
    customers: list[list[int]] = [[5, 2], [5, 4], [10, 3], [20, 1]]
    res: float = sol.averageWaitingTime(customers)
    print(res)


if __name__ == "__main__":
    main()
