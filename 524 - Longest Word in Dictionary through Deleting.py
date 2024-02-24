from collections import Counter


class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        longest_word: str = ""
        dict_input: dict = Counter(s)

        for item in dictionary:
            if len(longest_word) > len(item):
                continue

            dict_word: dict = Counter(item)
            if self.isWordValid(dict_word, dict_input, item, s):
                if longest_word == "" or len(longest_word) < len(item):
                    longest_word = item
                else:
                    longest_word = min(item, longest_word)

        return longest_word

    def isWordValid(
        self, dict_word: dict, dict_input: dict, word: str, input_str: str
    ) -> bool:
        for letter in dict_word:
            if letter not in dict_input:
                return False
            if dict_word[letter] > dict_input[letter]:
                return False

        word_combo: str = ""
        word_index: int = 0
        input_index: int = 0

        while input_index < len(input_str):
            if input_str[input_index] == word[word_index]:
                word_combo += word[word_index]

                if word_combo == word:
                    return True
                word_index += 1
            input_index += 1

        return False


def main():
    sol = Solution()

    s: str = "aewfafwafjlwajflwajflwafj"
    dictionary: list[str] = [
        "apple",
        "ewaf",
        "awefawfwaf",
        "awef",
        "awefe",
        "ewafeffewafewf",
    ]
    result: str = sol.findLongestWord(s, dictionary)
    print(result)


if __name__ == "__main__":
    main()
