from collections import deque


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        possibilities: set[str] = set()
        l: int = 0

        while l <= len(s):
            r: int = l + 1
            while r <= len(s):
                part: str = s[l:r]
                if self.isPalindrome(part):
                    possibilities.add(part)

                r += 1
            l += 1

        # start, end, possibilities
        q: list[tuple[int, int, list[str]]] = [(0, 0, [])]
        dq = deque(q)
        result: list[list[str]] = []

        while dq:
            start, end, arr = dq.popleft()

            if end > len(s):
                if sum([len(item) for item in arr]) == len(s):
                    result.append(arr)
                continue

            if s[start:end] in possibilities:
                res: list[str] = arr.copy()
                res.append(s[start:end])
                dq.append((end, end + 1, res))

            dq.append((start, end + 1, arr))

        return result

    def isPalindrome(self, s: str) -> bool:
        l: int = 0
        r: int = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


def main() -> None:
    sol = Solution()
    s = "ababa"
    res: list[list[str]] = sol.partition(s)
    print(res)


if __name__ == "__main__":
    main()
