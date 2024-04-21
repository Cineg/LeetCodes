class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:

        seen: set = set()
        nodes: dict[int, list[int]] = self.get_linked_nodes(edges)
        return self.walk(source, nodes, destination, seen)

    def walk(
        self, curr: int, nodes: dict[int, list[int]], dest: int, seen: set
    ) -> bool:
        if curr == dest:
            return True

        seen.add(curr)
        for item in nodes[curr]:
            if item not in seen:
                if self.walk(item, nodes, dest, seen):
                    return True

        return False

    def get_linked_nodes(self, edges: list[list[int]]) -> dict[int, list[int]]:
        nodes: dict[int, list[int]] = {}
        for x, y in edges:
            if x not in nodes:
                nodes[x] = [y]
            if x in nodes:
                nodes[x].append(y)

            if y not in nodes:
                nodes[y] = [x]
            if y in nodes:
                nodes[y].append(x)

        return nodes


def main():
    sol = Solution()
    list = [
        [0, 7],
        [0, 8],
        [6, 1],
        [2, 0],
        [0, 4],
        [5, 8],
        [4, 7],
        [1, 3],
        [3, 5],
        [6, 5],
    ]
    n = 10
    source = 7
    destination = 5

    res = sol.validPath(n, list, source, destination)
    print(res)


if __name__ == "__main__":
    main()
