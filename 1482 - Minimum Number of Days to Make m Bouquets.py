class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        minimum_flowers: int = m * k
        if minimum_flowers > len(bloomDay):
            return -1

        left: int = 0
        right: int = max(bloomDay)

        while left < right:
            day: int = left + (right - left) // 2
            if self.possible(bloomDay, day, m, k):
                right = day
            else:
                left = day + 1
        return left

    def possible(self, bloomDay: list[int], day: int, m: int, k: int) -> bool:
        bq: int = 0
        flowers: int = 0

        for bloom in bloomDay:
            if bloom > day:
                flowers = 0  # reset counter
            else:
                bq += (flowers + 1) // k
                flowers = (flowers + 1) % k

        return bq >= m


def main():
    sol = Solution()
    bloomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3

    res = sol.minDays(bloomDay, m, k)
    print(res)


if __name__ == "__main__":
    main()
