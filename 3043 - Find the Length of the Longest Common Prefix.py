class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.child: dict[int, Node] = {}


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        root: Node = Node(0)

        for item in arr1:
            node: Node = root
            for i in [int(x) for x in str(item)]:
                if i not in node.child:
                    node.child[i] = Node(i)

                node = node.child[i]

        longest_prefix: int = 0
        for item in arr2:
            node = root
            res: int = self._get_prefix([int(x) for x in str(item)], node)
            longest_prefix = max(res, longest_prefix)

        return longest_prefix

    def _get_prefix(self, item: list[int], node: Node) -> int:
        i: int = 0
        while i < len(item):
            if item[i] not in node.child:
                return i

            node = node.child[item[i]]
            i += 1

        return i


def main() -> None:
    arr1: list[int] = [1, 10, 100]
    arr2: list[int] = [1000]

    print(Solution().longestCommonPrefix(arr1, arr2))


if __name__ == "__main__":
    main()
