class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice: int = 0
        bob: int = 0

        for index in range(1, len(colors) - 1):
            if colors[index - 1] == colors[index] == colors[index + 1]:
                if colors[index] == "A":
                    alice += 1
                else:
                    bob += 1
            
        return alice > bob


def main() -> None:
    sol = Solution()
    result: bool = sol.winnerOfGame("AABBBABBAAAAAAAAAAABAAAAABBBBBBABBBBAABBBBABAABBBABBABABBBAAABBABBBBBAABAABBBBBBBAABAAABAAAAAAABAABBABAABBABABAABBBBAABABBABBBBABAABBABBBBAABBABAABBABBAAAABBBBBBBAABABBBAABBAAAAAABABBABBBABBBBBAABAAAABAABABBBABBABAABBBBABBABBBAABABABABBAABBAABBAAAABBAABAAABABAABBBAAAAABABAABABAAB")
    print(result)

if __name__ == "__main__":
    main()