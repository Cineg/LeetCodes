class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        if len(haystack) < len(needle):
            return -1

        for hay_index, letter in enumerate(haystack):
            if result != -1:
                return result
        
            if len(haystack) - hay_index - len(needle) < 0:
                return result
            
            if letter == needle[0]:
                for nee_index, matches in enumerate(needle):
                    result = hay_index
                    if haystack[hay_index + nee_index] != matches:
                        result = -1
                        break

        return result
    
def main():
    sol = Solution()
    print(sol.strStr("mississippi", "issipi"))
    

if __name__ == "__main__":
    main()