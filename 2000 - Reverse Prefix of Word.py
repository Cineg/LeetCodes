class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx: int = 0

        while idx < len(word):
            if word[idx] == ch:
                break
            idx += 1

        if idx >= len(word):
            return word

        return word[idx::-1] + word[idx + 1 : :]


def main() -> None:
    sol = Solution()
    word: str = "abcdefd"
    ch: str = "d"

    res: str = sol.reversePrefix(word, ch)
    print(res)


if __name__ == "__main__":
    main()
