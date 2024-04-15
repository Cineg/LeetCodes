# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Node:
    def __init__(self, char: str) -> None:
        self.val: str = char
        self.isWord: bool = False
        self.child: list[Node | None] = [None] * 26


class Trie:

    def __init__(self) -> None:
        self.root = Node("")

    def insert(self, word: str) -> None:
        node: Node = self.root

        for char in word:
            index: int = self._get_letter_num(char)

            if node.child[index] == None:
                node.child[index] = Node(char)

            node = node.child[index]

        node.isWord = True

    def search(self, word: str) -> bool:
        node: Node = self.root

        for char in word:
            index: int = self._search_char(char, node)
            if index < 0:
                return False

            node = node.child[index]

        return True if node.isWord else False

    def startsWith(self, prefix: str) -> bool:
        node: Node = self.root

        for char in prefix:
            index: int = self._search_char(char, node)
            if index < 0:
                return False
            node = node.child[index]

        return True

    def _get_letter_num(self, char: str) -> int:
        return ord(char) - 97

    def _search_char(self, char: str, node: Node) -> int:
        index: int = self._get_letter_num(char)
        if node.child[index] == None:
            return -1
        return index


def main():
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))


if __name__ == "__main__":
    main()
