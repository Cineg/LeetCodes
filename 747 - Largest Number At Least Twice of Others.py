class Solution:
    def dominantIndex(self, nums: list[int]) -> int:

        largest_index: int = -1
        largest_num: int = -1
        second_largest: int = -1

        i: int = 0
        while i < len(nums):
            if nums[i] > largest_num:
                second_largest = largest_num
                largest_num = nums[i]
                largest_index = i
            elif nums[i] > second_largest:
                second_largest = nums[i]

            i += 1

        if second_largest * 2 <= largest_num:
            return largest_index

        return -1
