import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap: list[int] = []

        while nums:
            num: int = nums.pop()
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


def main() -> None:
    sol = Solution()
    nums: list[int] = [3, 2, 1, 5, 6, 4]
    k = 2

    res: int = sol.findKthLargest(nums, k)
    print(res)


if __name__ == "__main__":
    main()
