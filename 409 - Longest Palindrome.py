class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq: dict[str, int] = {}
        res: int = 0
        for char in s:
            if char in freq:
                freq[char] += 1
                if freq[char] % 2 == 0:
                    res += 2
            else:
                freq[char] = 1

        for c in freq.values():
            if c % 2:
                res += 1
                break

        return res
