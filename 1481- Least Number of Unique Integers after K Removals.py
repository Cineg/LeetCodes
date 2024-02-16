from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        items = Counter(arr)

        count: list[int] = []
        for item in items:
            count.append(items[item])

        count.sort()

        while k > 0:
            if count[0] > k:
                break

            k -= count[0]
            count.pop(0)

        print(len(count))
        return len(count)


def main():
    sol = Solution()
    sol.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3)


if __name__ == "__main__":
    main()
