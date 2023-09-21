class Solution:
    def frequencySort(self, s: str) -> str:
        dctLetters = {}
        dctLetters = dict.fromkeys(s, 0)
        for letter in s:
            if letter in dctLetters:
                dctLetters[letter] += 1

        dctSorted = sorted(dctLetters.items(), key=lambda x: x[1])

        strResult = ''
        for letter, value in reversed(dctSorted):
            for i in range(value):
                strResult += letter

        return strResult
