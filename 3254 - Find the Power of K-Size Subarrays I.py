class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        arr: list[int] = []
        i: int = 0
        while i < len(nums) - (k - 1):
            arr.append(self._get_largest(nums[i : i + k]))
            i += 1

        return arr

    def _get_largest(self, nums: list[int]) -> int:
        i: int = 1
        while i < len(nums):
            if nums[i] <= nums[i - 1] or nums[i - 1] + 1 != nums[i]:
                return -1
            i += 1

        return nums[-1]


def main() -> None:
    nums: list[int] = [2, 2, 2, 2, 2]
    k: int = 4
    print(Solution().resultsArray(nums, k))


if __name__ == "__main__":
    main()
