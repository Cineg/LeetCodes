from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter: dict[str, int] = Counter(t)
        min_str: str = ""

        l: int = 0
        r: int = 0
        while r <= len(s):

            if max(counter.values()) <= 0:
                if min_str == "":
                    min_str = s[l:r]

                if len(s[l:r]) < len(min_str):
                    min_str = s[l:r]

                if s[l] in counter:
                    counter[s[l]] += 1

                l += 1
                continue

            if len(s) == r:
                break

            if s[r] in counter:
                counter[s[r]] -= 1
            r += 1

        return min_str


def main() -> None:
    sol = Solution()
    s: str = "ADOBECODEBANC"
    t: str = "ABC"
    res: str = sol.minWindow(s, t)
    print(res)


if __name__ == "__main__":
    main()
