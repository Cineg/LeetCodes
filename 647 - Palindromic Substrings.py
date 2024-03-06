class Solution:
    def countSubstrings(self, s: str) -> int:
        l_pointer: int = 0

        count: int = 0
        while l_pointer < len(s) + 1:
            r_pointer: int = l_pointer + 1
            while r_pointer < len(s) + 1:
                if len(s[l_pointer:r_pointer]) == 1:
                    count += 1
                else:
                    new_s: str = s[l_pointer:r_pointer]
                    rev_s: str = new_s[::-1]

                    if new_s == rev_s:
                        count += 1

                r_pointer += 1

            l_pointer += 1

        return count


def main() -> None:
    sol: Solution = Solution()
    s: str = "abc"

    print(sol.countSubstrings(s))


if __name__ == "__main__":
    main()
