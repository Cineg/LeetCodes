class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        res: list[list[int]] = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    current_res: list[int] = [i, j]
                    self.walk(land, i, j, current_res)
                    res.append(current_res)

                    # clear res
                    for row in range(current_res[0], current_res[2] + 1):
                        for col in range(current_res[1], current_res[3] + 1):
                            land[row][col] = 0

        return res

    def walk(self, land: list[list[int]], r: int, c: int, result: list[int]) -> bool:
        if r >= len(land) or c >= len(land[0]):
            return False
        if land[r][c] == 0:
            return False

        if not self.walk(land, r + 1, c, result) and not self.walk(
            land, r, c + 1, result
        ):
            result.append(r)
            result.append(c)

        return True


def main() -> None:
    sol = Solution()
    land: list[list[int]] = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]

    res: list[list[int]] = sol.findFarmland(land)
    print(res)


if __name__ == "__main__":
    main()
