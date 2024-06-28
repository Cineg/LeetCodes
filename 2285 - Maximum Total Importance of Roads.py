import heapq


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        node_freq: dict = {}
        for x, y in roads:
            if x not in node_freq:
                node_freq[x] = 1
            else:
                node_freq[x] += 1

            if y not in node_freq:
                node_freq[y] = 1
            else:
                node_freq[y] += 1

        importance: list[tuple[int, int]] = [
            (-node_freq[key], key) for key in node_freq
        ]
        heapq.heapify(importance)

        while n > 0 and importance:
            val: tuple[int, int] = heapq.heappop(importance)
            node_freq[val[1]] = n
            n -= 1

        res: int = 0
        for x, y in roads:
            res += node_freq[x] + node_freq[y]

        return res


def main() -> None:
    sol = Solution()
    roads: list[list[int]] = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    n: int = 5

    res: int = sol.maximumImportance(n, roads)
    print(res)


if __name__ == "__main__":
    main()
