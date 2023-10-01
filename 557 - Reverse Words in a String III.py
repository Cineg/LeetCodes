class Solution:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split(" ")
        final_str: str = ""
        for i, word in enumerate(str_arr):
            final_str += word[::-1]

            if i != len(str_arr ) - 1:
                final_str += " "


        return final_str
        
    
def main():
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))

if __name__ == "__main__":
    main()