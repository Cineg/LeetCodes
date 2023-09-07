class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums: list[int] = nums1 + nums2
        nums.sort()
        
        result: float
        length: int = len(nums)
        if length % 2 == 0:
            mid1 = nums[length//2]
            mid2 = nums[(length//2) - 1]
            result = (mid1 + mid2) / 2
        else:
            mid = length//2
            result = nums[mid]
        return result

def main():
    sol = Solution()
    print(sol.findMedianSortedArrays([1,3], [2]))

if __name__ == "__main__":
    main()