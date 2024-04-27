class Solution:
    def maxArea(self, height: list[int]) -> int:
        l: int = 0
        r: int = len(height) - 1

        max_container: int = 0

        while l < r:
            min_border: int = min(height[l], height[r])
            idle_water: int = min_border * (r - l)

            max_container = max(idle_water, max_container)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_container


def main() -> None:
    sol = Solution()
    height: list[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    res = sol.maxArea(height)
    print(res)


if __name__ == "__main__":
    main()
