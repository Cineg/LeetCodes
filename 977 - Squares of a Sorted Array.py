class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for index, item in enumerate(nums):
            nums[index] = item * item

        nums.sort()
        return nums


def main():
    sol = Solution()
    nums: list[int] = [-4, -1, 0, 3, 10]
    sol.sortedSquares(nums)


if __name__ == "__main__":
    main()
