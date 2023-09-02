
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temporary_string = ""
        i = 0
        for index, string in enumerate(strs):
            if len(string) == 0:
                return ""
            if index == 0:
                temporary_string = string
                continue

            if len(temporary_string) > len(string):
                temporary_string = temporary_string[:len(string)]
            
            for i in range(len(temporary_string)):
                if string[i] != temporary_string[i]:
                    if i == 0:
                        return ""
                    
                    temporary_string = temporary_string[:i]
                    break

        return temporary_string
    
def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))

if __name__ == "__main__":
    main()