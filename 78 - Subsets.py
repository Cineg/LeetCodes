class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.res: list[list[int]] = []

        self.walk([], 0, nums)
        self.res.append([])
        return self.res

    def walk(self, curr: list[int], pos: int, nums: list[int]) -> None:

        # walk empty
        if pos == len(nums):
            return

        self.walk(curr, pos + 1, nums)
        arr: list[int] = curr.copy()

        # walk not empty
        arr.append(nums[pos])
        self.res.append(arr)
        self.walk(arr, pos + 1, nums)

        return


def main() -> None:
    sol = Solution()
    nums: list[int] = [1, 2, 3]
    res: list[list[int]] = sol.subsets(nums)
    print(res)


if __name__ == "__main__":
    main()
