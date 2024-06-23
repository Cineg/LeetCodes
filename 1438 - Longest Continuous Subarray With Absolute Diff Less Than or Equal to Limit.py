import heapq


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        l: int = 0

        min_heap: list[tuple[int, int]] = []
        max_heap: list[tuple[int, int]] = []

        max_size: int = 1
        for r, num in enumerate(nums):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (-nums[r], r))

            while min_heap[0][1] < l:
                heapq.heappop(min_heap)
            while max_heap[0][1] < l:
                heapq.heappop(max_heap)

            if abs(-max_heap[0][0] - min_heap[0][0]) <= limit:
                max_size = max(max_size, r - l + 1)
            else:
                l += 1

        return max_size


def main() -> None:
    sol = Solution()
    nums: list[int] = [1, 5, 6, 7, 8, 10, 6, 5, 6]
    limit = 4
    res: int = sol.longestSubarray(nums, limit)
    print(res)


if __name__ == "__main__":
    main()
