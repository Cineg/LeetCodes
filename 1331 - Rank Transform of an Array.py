class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr: list[int] = sorted(arr.copy())
        rank: dict[int, int] = {}

        i: int = 0
        for item in sorted_arr:
            if item not in rank:
                i += 1
                rank[item] = i

        i = 0
        while i < len(arr):
            arr[i] = rank[arr[i]]
            i += 1

        return arr
