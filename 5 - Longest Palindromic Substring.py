class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest: int = 1
        palindrome: str = s[0]

        i: int = 0
        while i < len(s):
            j: int = i + longest
            while j <= len(s):
                ch: str = s[i:j]
                if ch == ch[::-1]:
                    longest = max(len(ch), longest)
                    palindrome = ch
                j += 1
            i += 1

        return palindrome


def main():
    sol = Solution()
    print(sol.longestPalindrome("bb"))


if __name__ == "__main__":
    main()
