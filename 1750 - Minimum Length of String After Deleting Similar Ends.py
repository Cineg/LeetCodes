class Solution:
    def minimumLength(self, s: str) -> int:
        while True:
            l_index: int = 0
            r_index: int = len(s) - 1

            if l_index < 0 or r_index < 0 or len(s) == 0:
                return 0

            if l_index == r_index:
                return len(s)

            if s[l_index] == s[r_index]:

                while l_index < r_index - 1:
                    if s[l_index] == s[l_index + 1]:
                        l_index += 1
                    else:
                        break

                while r_index > l_index + 1:
                    if s[r_index] == s[r_index - 1]:
                        r_index -= 1
                    else:
                        break

                s = s[l_index + 1 : r_index]

            else:
                return len(s)


def main() -> None:
    sol: Solution = Solution()
    s: str = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"

    print(sol.minimumLength(s))


if __name__ == "__main__":
    main()
