class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l: int = 0
        r: int = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            if numbers[l] + numbers[r] > target:
                r -= 1

            if numbers[l] + numbers[r] < target:
                l += 1

        return [-1, -1]


def main() -> None:
    sol = Solution()
    nums: list[int] = [2, 7, 11, 15]
    target: int = 9
    res: list[int] = sol.twoSum(nums, target)
    print(res)


if __name__ == "__main__":
    main()
