class Solution:
    def removeStars(self, s: str) -> str:
        i: int = 0
        result: str = ""

        while True:
            if i >= len(s):
                break
            
            if s[i] == "*":
                if len(result) > 0:
                    result = result[:-1]
                else:
                    result = ""
            else:
                result = result + s[i]

            i += 1

        return result

def main() -> None:
    sol = Solution()
    solution: str = sol.removeStars("abc***")

if __name__ == "__main__":
    main()