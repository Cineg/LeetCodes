class Node:
    def __init__(self, isWord: bool = False) -> None:
        self.nodes: list[Node | None] = [None] * 26
        self.isWord: bool = isWord


class WordDictionary:
    def __init__(self) -> None:
        self.words: Node = Node()

    def addWord(self, word: str) -> None:
        current_node: Node = self.words
        for idx, letter in enumerate(word):
            l_idx: int = ord(letter) - 97

            if current_node.nodes[l_idx] == None:
                current_node.nodes[l_idx] = Node()

            current_node = current_node.nodes[l_idx]

            if idx == len(word) - 1:
                current_node.isWord = True

    def search(self, word: str) -> bool:
        node: Node = self.words
        return self._search(word, node)

    def _search(self, word: str, node: Node) -> bool:
        for idx, letter in enumerate(word):

            if letter == ".":
                return self._wildcard_search(node, word[idx + 1 : :])

            l_idx: int = ord(letter) - 97

            if not node.nodes[l_idx]:
                return False

            node = node.nodes[l_idx]

        return node.isWord

    def _wildcard_search(self, node: Node, remaining: str) -> bool:
        for wild_node in node.nodes:
            if wild_node != None:
                if self._search(remaining, wild_node):
                    return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


def main() -> None:
    sol = WordDictionary()
    sol.addWord("bad")
    sol.addWord("dad")
    sol.addWord("mad")
    print(sol.search("pad"))
    print(sol.search("bad"))
    print(sol.search(".ad"))
    print(sol.search("b.."))


if __name__ == "__main__":
    main()
