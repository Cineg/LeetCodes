class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        d = {}
        words = s1.split(" ")
        words += s2.split(" ")

        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

        return [word for word, occurences in d.items() if occurences == 1]
