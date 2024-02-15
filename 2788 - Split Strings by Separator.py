class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        total: list = []
        for word in words:
            splitted_words: list[str] = word.split(separator)
            for item in splitted_words:
                if len(item) > 0:
                    total.append(item)

        return total
