class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for character in s:
            if character in "{[(":
                list.append(character)
            else:
                if len(list) == 0: 
                    return False

                if character == ")" and list[-1] != "(" or character == "]" and list[-1] != "[" or  character == "}" and list[-1] != "{":
                    return False

                list.pop()
                
        return not list

def main():
    Test = "{[]}"
    solution = Solution()
    print(solution.isValid(Test))
    
if __name__ == "__main__":
    main()