from typing import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        nums.sort(key=lambda x: (freq[x], -x))
        return nums


def main():
    sol = Solution()
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    res = sol.frequencySort(nums)
    print(res)


if __name__ == "__main__":
    main()
