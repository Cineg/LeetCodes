class Solution:
    def findMin(self, nums: list[int]) -> int:

        def walk(nums: list[int], lo: int, hi: int) -> int:
            if lo >= hi:
                return nums[lo]

            mid: int = lo + (hi - lo) // 2

            if nums[hi] < nums[mid]:
                return walk(nums, mid + 1, hi)
            elif nums[lo] <= nums[mid]:
                return walk(nums, lo, mid)

            return min(walk(nums, mid + 1, hi), walk(nums, lo, mid))

        return walk(nums, 0, len(nums) - 1)


def main() -> None:
    sol: Solution = Solution()
    nums: list[int] = [5, 1, 2, 3, 4]
    res: int = sol.findMin(nums)

    print(res)


if __name__ == "__main__":
    main()
