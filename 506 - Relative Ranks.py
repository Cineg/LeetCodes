class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        res: list[int] = score[::]
        res.sort(reverse=True)

        d: dict[int, str] = {}
        for i, s in enumerate(res):
            val: str = str(i + 1)
            if i == 0:
                val = "Gold Medal"
            elif i == 1:
                val = "Silver Medal"
            elif i == 2:
                val = "Bronze Medal"

            d[s] = val

        result: list[str] = []
        for s in score:
            result.append(d[s])

        return result
