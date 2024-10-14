from heapq import heapify, heappush, heappop
import math


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        heap: list[int] = [-num for num in nums]
        heapify(heap)
        res: int = 0
        while k > 0:
            num: int = heappop(heap)
            res -= num
            heappush(heap, math.floor(num / 3))
            k -= 1

        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [1, 10, 3, 3, 3]
    k: int = 3
    print(sol.maxKelements(nums, k))


if __name__ == "__main__":
    main()
