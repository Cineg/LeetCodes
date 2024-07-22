class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        l: list[tuple[int, str]] = []
        for i in range(len(names)):
            l.append((heights[i], names[i]))

        l.sort(reverse=True)
        return [x[1] for x in l]
