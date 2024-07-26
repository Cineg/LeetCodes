class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:

        distance_matrix: list[list[float]] = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            # distance to self
            distance_matrix[i][i] = 0

        for i, j, w in edges:
            distance_matrix[i][j] = w
            distance_matrix[j][i] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (
                        distance_matrix[i][j]
                        > distance_matrix[i][k] + distance_matrix[k][j]
                    ):
                        distance_matrix[i][j] = (
                            distance_matrix[i][k] + distance_matrix[k][j]
                        )

        best_city: int = -1
        min_cities: float = float("inf")
        for i in range(n):
            cities: int = 0
            for j in range(n):
                if distance_matrix[i][j] <= distanceThreshold:
                    cities += 1

            if cities <= min_cities:
                min_cities = cities
                best_city = i

        return best_city


def main():
    sol = Solution()
    n: int = 4
    edges: list[list[int]] = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold: int = 4
    res: int = sol.findTheCity(n, edges, distanceThreshold)
    print(res)


if __name__ == "__main__":
    main()
