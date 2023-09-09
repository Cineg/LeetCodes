class Solution:
    def intToRoman(self, num: int) -> str:
        roman_letters: dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        string: str = ""
        while num != 0:
            for key in roman_letters:
                if num / key >= 1:
                    string += roman_letters[key]
                    num -= key
                    break

        return string
    
def main():
    sol = Solution()
    print(sol.intToRoman(14))

if __name__ == "__main__":
    main()
