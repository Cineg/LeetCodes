class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = 0
        stack: list[int] = []
        res: list[str] = []

        while i < len(s):
            if s[i] == "(":
                stack.append(len(res))
            elif s[i] == ")":
                start_idx: int = stack.pop()
                res[start_idx:] = res[start_idx:][::-1]
            else:
                res.append(s[i])

            i += 1

        return "".join(res)
