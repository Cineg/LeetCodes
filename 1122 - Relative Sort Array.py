from typing import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq: dict[int, int] = Counter(arr1)

        res: list[int] = []
        for item in arr2:
            while freq[item] > 0:
                res.append(item)
                freq[item] -= 1

        temp_res: list[int] = []
        for item in freq:
            if freq[item] != 0:
                while freq[item] > 0:
                    temp_res.append(item)
                    freq[item] -= 1

        temp_res.sort()
        return res + temp_res
