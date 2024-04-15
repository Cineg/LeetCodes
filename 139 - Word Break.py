class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        results: dict = {}
        return self.walk(s, wordDict, results)

    def walk(self, s: str, words: list[str], results: dict) -> bool:
        if s in results:
            return results[s]

        if s in words:
            return True

        for i in range(1, len(s)):
            curr: str = s[:i]
            if curr in words and self.walk(s[i:], words, results):
                results[curr] = True
                return True

        results[s] = False
        return False


def main():
    sol = Solution()
    s: str = "catsandog"
    arr = ["cats", "dog", "sand", "and", "cat"]

    res = sol.wordBreak(s, arr)
    print(res)


if __name__ == "__main__":
    main()
