class Solution:
    def isPalindrome(self, s: str) -> bool:
        zero: int = ord("0")
        nine: int = ord("9")
        a: int = ord("a")
        z: int = ord("z")

        l: int = 0
        r: int = len(s) - 1

        while l < r:
            if not a <= ord(s[l].lower()) <= z and not zero <= ord(s[l]) <= nine:
                l += 1
                continue
            if not a <= ord(s[r].lower()) <= z and not zero <= ord(s[r]) <= nine:
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


def main() -> None:
    sol = Solution()
    print(ord("0"), ord("9"), ord("a"), ord("z"))
    s = "0P"

    print(sol.isPalindrome(s))


if __name__ == "__main__":
    main()
