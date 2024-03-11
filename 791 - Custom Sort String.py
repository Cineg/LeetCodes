class Solution:
    def customSortString(self, order: str, s: str) -> str:
        val: dict = self._create_dict(order)
        arr: list[str] = list(s)

        while True:
            i: int = 0
            changed: bool = False

            while i < len(arr) - 1:
                val1: int = self._assign_value(val, arr[i])
                val2: int = self._assign_value(val, arr[i + 1])

                if val1 > val2:
                    temp: str = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                    changed = True

                i += 1
            if not changed:
                break

        return "".join(arr)

    def _create_dict(self, order: str) -> dict:
        dic: dict = {}
        for index, letter in enumerate(order):
            dic[letter] = index

        return dic

    def _assign_value(self, dic: dict, val: str) -> int:
        if val not in dic:
            return 999
        else:
            return dic[val]


def main() -> None:
    sol: Solution = Solution()
    order: str = "cba"
    sort_string: str = "abcd"

    print(sol.customSortString(order, sort_string))


if __name__ == "__main__":
    main()
