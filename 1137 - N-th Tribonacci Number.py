class Solution:
    def tribonacci(self, n: int) -> int:
        data: list[int] = [0, 1, 1]

        if not self.walk(n, data):
            return -1

        return data[n]

    def walk(self, n: int, data: list[int]) -> bool:
        idx: int = len(data)

        if idx - 1 >= n:
            return True

        next_num: int = data[idx - 1] + data[idx - 2] + data[idx - 3]
        data.append(next_num)

        if self.walk(n, data) == True:
            return True

        return False


def main():
    sol = Solution()
    n = 4
    sol.tribonacci(n)


if __name__ == "__main__":
    main()
