class Solution:
    def minDeletions(self, s: str) -> int:
        dic: dict = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1

        used_frequencies: set = set()
        deletions: int = 0
        for character, frequency in dic.items():
            while frequency > 0 and frequency in used_frequencies:
                frequency -= 1
                deletions += 1

            used_frequencies.add(frequency)

        return deletions


def main():
    sol = Solution()
    sol.minDeletions("abbccccdddd")

if __name__ == "__main__":
    main()