class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre: list[int] = [1] * len(nums)
        post: list[int] = [1] * len(nums)
        res: list[int] = []

        if len(nums) <= 1:
            return nums

        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = nums[i] * pre[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post[i] = nums[i]
            else:
                post[i] = nums[i] * post[i + 1]

        for i in range(len(nums)):
            if i == 0:
                res.append(post[1])
                continue
            if i == len(nums) - 1:
                res.append(pre[i - 1])
                continue

            val: int = pre[i - 1] * post[i + 1]
            res.append(val)

        return res


def main():
    sol = Solution()
    res = sol.productExceptSelf([1, 2, 3, 4])
    print(res)


if __name__ == "__main__":
    main()
