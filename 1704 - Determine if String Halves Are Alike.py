class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # split string in half
        halfPoint = len(s)//2
        string1 = slice(0, halfPoint)
        string2 = slice(halfPoint, len(s))

        return self.countVowels(self, s[string1]) == self.countVowels(self, s[string2])

    def countVowels(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c = 0
        for letter in s:
            if letter in vowels:
                c += 1
        return c


def main():
    objSolution = Solution
    s = "book"
    print(objSolution.halvesAreAlike(Solution, s))


if __name__ == '__main__':
    main()
