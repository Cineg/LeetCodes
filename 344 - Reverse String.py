class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l: int = 0
        r: int = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1
