class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        l: int = 0
        sub_count: int = 0
        res: int = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                k -= 1
                sub_count = 0

            while k == 0:
                if nums[l] % 2 == 1:
                    k += 1
                sub_count += 1

                l += 1

            res += sub_count
        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k: int = 2
    res: int = sol.numberOfSubarrays(nums, k)
    print(res)


if __name__ == "__main__":
    main()
