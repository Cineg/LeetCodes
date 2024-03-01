class Solution:
    def isNumber(self, s: str) -> bool:
        valid_nums: set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        decimal_index: int = -1
        e_index: int = -1
        num: bool = False
        index: int = 0

        while index < len(s):
            char: str = s[index]

            if char not in valid_nums:
                if char in "+-" and index == 0:
                    pass

                elif char == "." and decimal_index == -1:
                    if e_index != -1 and e_index < index:
                        return False

                    decimal_index = index

                elif char in "eE" and e_index == -1:
                    if index == 0:
                        return False

                    if s[index - 1] not in valid_nums:
                        if s[index - 1] != ".":
                            return False
                        if s[index - 1] == "." and num == False:
                            return False

                    if index + 1 >= len(s):
                        return False

                    elif s[index + 1] not in valid_nums:
                        if s[index + 1] in "+-" and index + 2 < len(s):
                            if s[index + 2] not in valid_nums:
                                return False
                            else:
                                index += 1
                        else:
                            return False

                    e_index = index

                else:
                    return False

            elif num == False and char in valid_nums:
                num = True

            index += 1

        return num


def main() -> None:
    sol = Solution()
    s = "005047e+6"
    print(sol.isNumber(s))


if __name__ == "__main__":
    main()
