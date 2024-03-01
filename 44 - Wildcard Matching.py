class Solution:
    def isMatch(self, input_string: str, pattern: str) -> bool:
        p_index: int = 0
        s_index: int = 0
        last_star: int = -1
        last_match: int = 0

        while s_index < len(input_string):

            if p_index < len(pattern) and (
                input_string[s_index] == pattern[p_index] or pattern[p_index] == "?"
            ):
                p_index += 1
                s_index += 1

            elif p_index < len(pattern) and pattern[p_index] == "*":
                last_star = p_index
                last_match = s_index
                p_index += 1

            elif last_star != -1:
                p_index = last_star + 1
                last_match += 1
                s_index = last_match

            else:
                return False

        if p_index < len(pattern):
            while p_index < len(pattern):
                if pattern[p_index] != "*":
                    return False
                p_index += 1

        return True


def main():
    sol: Solution = Solution()
    input_string: str = "aa"
    pattern: str = "*"

    print(sol.isMatch(input_string, pattern))


if __name__ == "__main__":
    main()
