import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap: list[tuple[int, list[int]]] = []
        for point in points:
            x1, x2 = point
            dist: int = (x1 * x1) + (x2 * x2)
            heap.append((dist, [x1, x2]))

        heapq.heapify(heap)

        res: list[list[int]] = []
        for i in range(k):
            _, val = heapq.heappop(heap)
            res.append(val)

        return res


def main() -> None:
    sol = Solution()
    points: list[list[int]] = [
        [68, 97],
        [34, -84],
        [60, 100],
        [2, 31],
        [-27, -38],
        [-73, -74],
        [-55, -39],
        [62, 91],
        [62, 92],
        [-57, -67],
    ]
    k = 5

    res: list[list[int]] = sol.kClosest(points, k)
    print(res)


if __name__ == "__main__":
    main()
