class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        i: int = 0

        while i < len(tokens):
            if tokens[i] in ["+", "-", "/", "*"]:
                int1: int = int(tokens[i - 2])
                int2: int = int(tokens[i - 1])
                if tokens[i] == "+":
                    tokens[i - 2] = str(int1 + int2)
                if tokens[i] == "-":
                    tokens[i - 2] = str(int1 - int2)
                if tokens[i] == "*":
                    tokens[i - 2] = str(int1 * int2)
                if tokens[i] == "/":
                    tokens[i - 2] = str(int(int1 / int2))

                tokens.pop(i - 1)
                tokens.pop(i - 1)

                i -= 2
            i += 1

        return int(tokens[0])


def main():
    sol: Solution = Solution()
    tokens: list[str] = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "/",
        "*",
        "17",
        "+",
        "5",
        "+",
    ]
    sol.evalRPN(tokens)


if __name__ == "__main__":
    main()
