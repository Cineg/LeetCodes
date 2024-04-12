class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2:
            return 0

        l: int = 0
        r: int = len(height) - 1

        l_max: int = height[l]
        r_max: int = height[r]

        res: int = 0

        while l <= r:
            if height[l] > l_max:
                l_max = height[l]
            if height[r] > r_max:
                r_max = height[r]

            if l_max <= r_max:
                res += l_max - height[l]
                l += 1
            else:
                res += r_max - height[r]
                r -= 1

        return res


def main():
    sol = Solution()

    # arr = [4, 2, 0, 3, 2, 5]
    # arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    arr = [4, 9, 4, 5, 3, 2]
    print(sol.trap(arr))


if __name__ == "__main__":
    main()
