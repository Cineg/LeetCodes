from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        cnt: dict = Counter(nums)
        arr: list = []
        for item in cnt:
            if len(arr) == 2:
                break
            if cnt[item] == 1:
                arr.append(item)

        return arr

    def singleNumber2(self, nums: list[int]) -> list[int]:
        seen: set[int] = set()
        for num in nums:
            if num not in seen:
                seen.add(num)

            elif num in seen:
                seen.remove(num)

        res: list[int] = []
        for num in seen:
            res.append(num)

        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [1, 2, 1, 3, 2, 5]

    res: list[int] = sol.singleNumber2(nums)
    print(res)


if __name__ == "__main__":
    main()
