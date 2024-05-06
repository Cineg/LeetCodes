from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        if len(s1) == len(s2):
            return Counter(s1) == Counter(s2)

        freq: dict[str, int] = Counter(s1)
        window: int = len(s1)
        left: int = 0

        while left + window <= len(s2):
            if Counter(s2[left : left + window]) == freq:
                return True

            left += 1

        return False


def main() -> None:
    sol = Solution()
    s1: str = "ab"
    s2: str = "eidbaooo"

    res: bool = sol.checkInclusion(s1, s2)
    print(res)


if __name__ == "__main__":
    main()
