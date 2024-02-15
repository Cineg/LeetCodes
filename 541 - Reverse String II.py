class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i: int = 0
        flag: bool = False

        reversed_str: str = ""

        while i < len(s):
            flag = not flag
            if flag:
                stamp: int = i

            index = 0

            slice: int = min(k, len(s[i:]))
            for index in range(slice):
                if slice == 1:
                    reversed_str += s[i]
                    i += 1
                    break

                if flag:
                    reversed_str += s[stamp + slice - (1 + index)]
                else:
                    reversed_str += s[i]

                i += 1
                if i >= len(s):
                    break

        return reversed_str


def main():
    sol = Solution()
    sol.reverseStr("abcdefg", 8)


if __name__ == "__main__":
    main()
