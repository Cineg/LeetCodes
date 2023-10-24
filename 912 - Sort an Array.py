class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        items: dict = {}
        minimum: int = 0
        maximum: int = 0
        result: list = []
        for item in nums:
            if item in items:
                items[item] = items[item] + 1
            else:
                items[item] = 1
                if len(items) == 1:
                    maximum = item
                    minimum = item
                elif item > maximum:
                    maximum = item
                elif item < minimum:
                    minimum = item
        
        for item in range(minimum, maximum + 1):
            if item in items:
                result.extend([item]*items[item])
        
        return result


def main() -> None:
    sol = Solution()
    sol.sortArray([2,1,3,7, 7, 7])

if __name__ == "__main__":
    main()