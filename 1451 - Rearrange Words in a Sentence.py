class Solution:
    def arrangeWords(self, text: str) -> str:

        words: list[str] = text.split(" ")
        return " ".join(sorted(words, key=len)).capitalize()

        # while True:
        #     change: bool = False
        #     index: int = 0
        #     while index < len(words) - 1:
        #         l: int = index
        #         r: int = index + 1
        #         if len(words[r]) < len(words[l]):
        #             words[r], words[l] = (
        #                 words[l],
        #                 words[r],
        #             )
        #             change = True
        #         index += 1

        #     if not change:
        #         break

        # return " ".join(words).capitalize()


def main():
    sol = Solution()
    inp: str = "To be or not to be"
    print(sol.arrangeWords(inp))


if __name__ == "__main__":
    main()
