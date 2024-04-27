class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        anchor: int = 0
        res: list[list[int]] = []
        seen: set = set()

        while anchor < len(nums):
            l: int = anchor + 1
            r: int = len(nums) - 1

            while l < r:
                temp: int = nums[anchor] + nums[l] + nums[r]
                if temp > 0:
                    r -= 1
                    continue
                if temp < 0:
                    l += 1
                    continue

                if temp == 0:
                    li: list | tuple = [nums[anchor], nums[l], nums[r]]
                    li.sort()
                    li = tuple(li)
                    if li not in seen:
                        seen.add(li)
                        res.append([nums[anchor], nums[l], nums[r]])

                    l += 1

            anchor += 1
        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [-1, 0, 1, 2, -1, -4]
    res: list[list[int]] = sol.threeSum(nums)
    print(res)


if __name__ == "__main__":
    main()
