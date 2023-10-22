from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count: dict = Counter(nums)

        for item in count:
            if count[item] == 1:
                return item


def main():
    sol = Solution()
    sol.singleNumber([2,2,3,2])

if __name__ == "__main__":
    main()