class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        i: int = 0
        results: dict = {}
        arr: list = []
        while i + 10 <= len(s):
            sequence: str = s[i : i + 10]
            if sequence in results:
                results[sequence] += 1

            else:
                results[sequence] = 0

            i += 1

        for item in results:
            if results[item] > 0:
                arr.append(item)

        return arr


def main():
    sol: Solution = Solution()
    s: str = "AAAAAAAAAAA"
    sol.findRepeatedDnaSequences(s)


if __name__ == "__main__":
    main()
