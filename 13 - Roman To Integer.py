class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        answer = 0
        for i in range(len(s)):
            ## need to have to check at least two letters, to check if we are substracting.
            ## The letter should have corresponding descending values. If they are not - substract value.
            if i < len(s) - 1 and dct[s[i]] < dct[s[i+1]]: 
                answer -= dct[s[i]]
            else:
                answer += dct[s[i]]

        return answer
    
def main(roman_number: str):
    solution = Solution()
    
    return solution.romanToInt(roman_number)

if __name__ == "__main__":
    roman_number: str = "MMCXXXVII"
    main(roman_number)