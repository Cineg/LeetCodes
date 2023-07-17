from typing import List


def main():
    strInput = 'au'

    print(lengthOfLongestSubstring(strInput))


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0
    if len(s) > 1:
        intLen = 1

    for i in range(len(s)):

        dctLetters = {}
        dctLetters[s[i]] = s[i]
        intTempLen = 1

        for j in range(i + 1, len(s)):
            # we can skip the iteration if we have less possibilities than we actually have matches
            if intLen > intTempLen + (len(s) - j):
                break

            if s[j] not in dctLetters:
                intTempLen += 1
                dctLetters[s[j]] = s[j]
            else:
                break
            if intTempLen > intLen:
                intLen = intTempLen

    return intLen


if __name__ == '__main__':
    main()
