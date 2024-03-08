from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counter: dict = Counter(nums)

        max_freq: int = 0
        max_freq_nums: int = 0
        for num in counter:
            if max_freq < counter[num]:
                max_freq = counter[num]
                max_freq_nums = 1
            elif max_freq == counter[num]:
                max_freq_nums += 1

        return max_freq_nums * max_freq
