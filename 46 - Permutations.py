class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            n: int = nums.pop(0)
            perms: list[list[int]] = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)
            nums.append(n)

        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [1, 2, 3]
    res: list[list[int]] = sol.permute(nums)
    print(res)


if __name__ == "__main__":
    main()
