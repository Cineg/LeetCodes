import math


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars: list[tuple[int, int]] = list(zip(position, speed))
        cars.sort(reverse=True)

        res: list = []

        for pos, sp in cars:
            turns: float = (target - pos) / sp
            if not res:
                res.append(turns)
                continue
            elif res[-1] < turns:
                res.append(turns)

        return len(res)


def main() -> None:
    sol = Solution()
    target: int = 31
    position: list[int] = [5, 26, 18, 25, 29, 21, 22, 12, 19, 6]
    speed: list[int] = [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]

    res: int = sol.carFleet(target, position, speed)
    print(res)


if __name__ == "__main__":
    main()
