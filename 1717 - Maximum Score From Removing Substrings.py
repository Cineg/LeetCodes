class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        first: str = ""
        second: str = ""
        if x > y:
            first = "ab"
            second = "ba"
            f_score = x
            s_score = y
        else:
            first = "ba"
            second = "ab"
            f_score = y
            s_score = x

        stack: list[str] = []
        res: int = 0
        for char in s:
            if char == first[1] and stack and stack[-1] == first[0]:
                stack.pop()
                res += f_score
            else:
                stack.append(char)

        new_stack: list[str] = []
        for char in stack:
            if char == second[1] and new_stack and new_stack[-1] == second[0]:
                new_stack.pop()
                res += s_score
            else:
                new_stack.append(char)

        return res
