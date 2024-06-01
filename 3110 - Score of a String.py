class Solution:
    def scoreOfString(self, s: str) -> int:
        i: int = 1

        score: int = 0
        while i < len(s):
            score += abs(ord(s[i]) - ord(s[i - 1]))
            i += 1

        return score
