class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        letters: dict = {}
        for index, letter in enumerate(order):
            letters[letter] = index
        
        for index in range(1, len(words)):
            max_range: int = min(len(words[index]), len(words[index-1]))
            i: int = 0
            while i < max_range:
                letter_previous: str = words[index-1][i]
                letter_current: str = words[index][i]

                if letters[letter_current] > letters[letter_previous]:
                    break

                if letters[letter_current] < letters[letter_previous]:
                    return False
                
                if i == max_range - 1 and len(words[index]) < len(words[index-1]):
                    return False

                i += 1
        
        return True


def main() -> None:
    sol = Solution()
    res = sol.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
    print(res)

if __name__ == "__main__":
    main()