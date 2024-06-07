class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        d: set = set(dictionary)

        res: list[str] = []
        sentence_list: list[str] = sentence.split(" ")
        for i, word in enumerate(sentence_list):
            temp: str = ""
            for idx in range(len(word)):
                temp += word[idx]
                if temp in d:
                    res.append(temp)
                    break

            else:
                res.append(word)

        return " ".join(res)


def main() -> None:
    sol = Solution()
    dictionary: list[str] = ["cat", "bat", "rat"]
    sentence: str = "the cattle was rattled by the battery"
    res: str = sol.replaceWords(dictionary, sentence)
    print(res)


if __name__ == "__main__":
    main()
