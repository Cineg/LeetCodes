class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def walk(nums: list[int], lo: int, hi: int, target: int) -> int:
            if lo == hi:
                if nums[lo] == target:
                    return lo
                return -1

            if nums[hi] == target:
                return hi
            if nums[lo] == target:
                return lo

            mid: int = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid

            if nums[lo] < target < nums[mid]:
                return walk(nums, lo, mid, target)
            elif nums[mid] < target < nums[hi]:
                return walk(nums, mid + 1, hi, target)
            elif nums[lo] > nums[mid] and (target > nums[mid] or target < nums[mid]):
                return walk(nums, lo, mid, target)
            else:
                return walk(nums, mid + 1, hi, target)

        return walk(nums, 0, len(nums) - 1, target)


def main() -> None:
    sol: Solution = Solution()
    nums: list[int] = [5, 1, 2, 3, 4]
    target: int = 1
    res: int = sol.search(nums, target)
    print(res)


if __name__ == "__main__":
    main()
