class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        freq: list[int] = [0] * k

        for num in arr:
            remainder: int = (num % k + k) % k
            freq[remainder] += 1

        if freq[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        return True


def main():
    arr: list[int] = [-10, 10]
    k: int = 2

    print(Solution().canArrange(arr, k))


if __name__ == "__main__":
    main()
