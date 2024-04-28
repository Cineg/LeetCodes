import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        hi: int = max(piles)
        lo: int = 0

        while lo <= hi:
            res: int = 0
            pivot: int = lo + (hi - lo) // 2

            if pivot == 0:
                return 1

            for pile in piles:
                res += math.ceil(pile / pivot)
                if res > h:
                    break

            if lo == hi:
                return pivot

            if res > h:
                lo = pivot + 1
            if res <= h:
                hi = pivot

        return 1


def main() -> None:
    sol: Solution = Solution()
    piles: list[int] = [
        831235932,
        437082868,
        576572631,
        529869153,
        55330371,
        511060323,
        581115062,
        931692072,
        600856556,
        519045509,
        504164418,
        431105822,
        580257183,
    ]
    h: int = 964065706

    res: int = sol.minEatingSpeed(piles, h)
    print(res)


if __name__ == "__main__":
    main()
