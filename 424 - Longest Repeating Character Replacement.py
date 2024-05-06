from typing import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq: dict[str, int] = {}
        l: int = 0
        r: int = 0
        res: int = 0
        while r < len(s):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            max_freq: int = max(freq.values())

            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res


def main() -> None:
    sol = Solution()
    k = 1
    s = "AABABBA"

    print(sol.characterReplacement(s, k))


if __name__ == "__main__":
    main()
