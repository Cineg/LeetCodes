class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq: dict[int, int] = {0: 0, 1: 0, 2: 0}
        for num in nums:
            freq[num] += 1

        idx: int = 0
        for num in [0, 1, 2]:
            while freq[num] > 0:
                freq[num] -= 1
                nums[idx] = num
                idx += 1
