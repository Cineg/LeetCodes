class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack: list[str] = []
        for letter in s:
            if len(stack) == 0:
                stack.append(letter)
                continue

            if letter == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(letter)

        return len(stack)
