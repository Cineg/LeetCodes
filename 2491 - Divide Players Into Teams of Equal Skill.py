class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        sorted_skill = sorted(skill)

        pairs = []
        while sorted_skill:
            pairs.append((sorted_skill.pop(), sorted_skill.pop(0)))

        target = sum(pairs[0])
        chemistry = 0
        for pair in pairs:
            if sum(pair) != target:
                return -1

            chemistry += pair[0] * pair[1]

        return chemistry
