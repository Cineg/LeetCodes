class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result: list[int] = []
        for index, num in enumerate(nums):
            if num == target and len(result) == 0:
                result.append(index)
            
            if num == target and len(result) == 1:
                result.append(index)
            
            if num == target and len(result) == 2:
                result[1] = index
            
            if num != target and len(result) > 0:
                break

        if len(result) == 0:
            return [-1, -1]
        
        if len(result) == 1:
            result.append(result[0])
            return result

        return result

def main() -> None:
    sol = Solution()
    print(sol.searchRange([2,2], 2))

if __name__ == "__main__":
    main()