class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        largest: int = 0

        # start_element, minimum element, length
        stack: list = []
        for i, h in enumerate(heights):
            start_index: int = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                largest = max(largest, height * (i - idx))
                start_index = idx

            stack.append((start_index, h))

        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))

        return largest


def main() -> None:
    sol = Solution()
    heights: list[int] = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]

    res: int = sol.largestRectangleArea(heights)
    print(res)


if __name__ == "__main__":
    main()
