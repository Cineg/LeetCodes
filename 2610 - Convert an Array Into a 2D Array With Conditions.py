class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = [[]]

        for num in nums:
            added: bool = False
            for arr in result:
                if num not in arr:
                    arr.append(num)
                    added = True
                    break

            if not added:
                result.append([num])

        return result
