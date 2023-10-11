from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        unpacked_s = Counter(s)
        unpacked_t = Counter(t)

        for item in unpacked_s:
            if unpacked_t[item] != unpacked_s[item]:
                return False

        return True