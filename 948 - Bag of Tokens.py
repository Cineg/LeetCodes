class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        l_index: int = 0
        r_index: int = len(tokens) - 1
        score: int = 0
        max_score: int = 0

        tokens.sort()

        while l_index <= r_index:
            if power >= tokens[l_index]:
                power -= tokens[l_index]
                score += 1
                max_score = max(score, max_score)
                l_index += 1
            elif score > 0:
                power += tokens[r_index]
                r_index -= 1
                score -= 1
            else:
                break

        return max_score
