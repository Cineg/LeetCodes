class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        robots: list[list] = [
            [positions[idx], healths[idx], directions[idx], idx]
            for idx in range(len(positions))
        ]

        robots.sort()

        stack: list[list] = []
        for robot in robots:
            if not stack:
                stack.append(robot)
            elif stack[-1][2] == robot[2]:
                stack.append(robot)
            elif stack[-1][2] == "L" and robot[2] == "R":
                stack.append(robot)

            else:
                toAdd: bool = True
                while True:
                    if not stack:
                        break
                    if robot[2] == "R":
                        break
                    if robot[2] == "L" and stack[-1][2] == "L":
                        break

                    elif robot[1] > stack[-1][1]:
                        robot[1] -= 1
                        stack.pop()
                    elif robot[1] == stack[-1][1]:
                        stack.pop()
                        toAdd = False
                        break
                    else:
                        stack[-1][1] -= 1
                        toAdd = False
                        break

                if toAdd:
                    stack.append(robot)

        return [robot[1] for robot in sorted(stack, key=lambda xD: xD[3])]


def main():
    sol = Solution()
    positions = [5, 4, 3, 2, 1]
    healths = [2, 17, 9, 15, 10]
    directions = "RRRRR"

    res = sol.survivedRobotsHealths(positions, healths, directions)
    print(res)


if __name__ == "__main__":
    main()
