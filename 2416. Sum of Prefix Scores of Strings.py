class Node:
    def __init__(self, value: str) -> None:
        self.value: str = value
        self.child: dict[str, Node] = {}
        self.count: int = 0


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie: Node = Node("root")
        for word in words:
            node: Node = trie
            for letter in word:
                if letter not in node.child:
                    node.child[letter] = Node(letter)
                node = node.child[letter]
                node.count += 1

        result: list[int] = [0] * len(words)
        for idx, word in enumerate(words):
            node = trie
            for letter in word:
                node = node.child[letter]
                result[idx] += node.count

        return result


if __name__ == "__main__":
    words: list[str] = ["abc", "ab", "bc", "b"]
    print(Solution().sumPrefixScores(words))
