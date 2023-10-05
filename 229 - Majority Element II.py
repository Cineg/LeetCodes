from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        min_len: float = len(nums) / 3
        counter = Counter(nums)
        result: list[int] = []
        for item in counter:
            if counter[item] > min_len and item not in result:
                result.append(item)

        return result
    

def main() -> None:
    sol = Solution()
    print(sol.majorityElement([3,2,3]))

if __name__ == "__main__":
    main()