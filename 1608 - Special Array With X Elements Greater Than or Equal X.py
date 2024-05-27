from typing import Counter


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        freq: dict[int, int] = Counter(nums)
        for i in range(len(nums) + 1):
            count: int = 0
            for item in freq:
                if item >= i:
                    count += freq[item]

            if count == i:
                return i

        return -1


def main() -> None:
    sol = Solution()
    nums: list[int] = [0, 4, 3, 0, 4]
    res: int = sol.specialArray(nums)
    print(res)


if __name__ == "__main__":
    main()
