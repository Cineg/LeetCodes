from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countOfOccurences = Counter(arr)
        uniqueNoOfOccurences = len(set(countOfOccurences.values()))
        return len(countOfOccurences) == uniqueNoOfOccurences


def main():
    objSolution = Solution
    arr = [1, 2, 2, 1, 1, 3, 3]
    print(objSolution.uniqueOccurrences(Solution, arr))


if __name__ == '__main__':
    main()
