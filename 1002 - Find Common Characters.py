class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        chars: list[dict[str, int]] = []
        used: set = set()

        for word in words:
            data = {}
            for letter in word:
                if letter in data:
                    data[letter] += 1
                else:
                    data[letter] = 1

                used.add(letter)

            chars.append(data)

        res: list[str] = []
        for letter in used:
            count: int = -1
            for word in chars:
                if letter not in word:
                    count = -1
                    break

                if letter in word:
                    if count == -1:
                        count = word[letter]
                    elif count > word[letter]:
                        count = word[letter]

            if count != -1:
                for _ in range(count):
                    res.append(letter)

        return res


def main() -> None:
    sol = Solution()
    words: list[str] = [
        "acabcddd",
        "bcbdbcbd",
        "baddbadb",
        "cbdddcac",
        "aacbcccd",
        "ccccddda",
        "cababaab",
        "addcaccd",
    ]

    res: list[str] = sol.commonChars(words)
    print(res)


if __name__ == "__main__":
    main()
