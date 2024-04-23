class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums: set = set(nums)

        longest_seq: int = 0

        for num in set_nums:
            if num - 1 in set_nums:
                continue

            seq: int = 1
            temp: int = num

            while True:
                temp += 1
                if temp not in set_nums:
                    break

                seq += 1

            longest_seq = max(longest_seq, seq)

        return longest_seq


def main():
    sol = Solution()
    nums: list[int] = [100, 4, 200, 1, 3, 2]
    sol.longestConsecutive(nums)


if __name__ == "__main__":
    main()
