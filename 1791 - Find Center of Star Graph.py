class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        if edges[0][0] in [edges[1][0], edges[1][1]]:
            return edges[0][0]
        return edges[0][1]

        # d: dict[int, list[tuple]] = {}
        # for x, y in edges:
        #     if x in d:
        #         d[x].append( (x, y))
        #     if x not in d:
        #         d[x] = [(x,y)]

        #     if y in d:
        #         d[y].append((y,x))
        #     if y not in d:
        #         d[y] = [(y,x)]

        # for point in d:
        #     if len(d[point]) > 1:
        #         return point
