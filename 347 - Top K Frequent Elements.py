from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq: dict[int, int] = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        temp: list[tuple[int, int]] = [(-freq[key], key) for key in freq]
        heapify(temp)

        res: list[int] = []
        for _ in range(k):
            item: int = heappop(temp)[1]
            res.append(item)

        return res


def main() -> None:
    sol = Solution()
    res: list[int] = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)

    print(res)


if __name__ == "__main__":
    main()
