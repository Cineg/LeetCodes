class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        total_len: int = len(s)
        all_possibilities: list[int] = [0] * (total_len + 1)

        for i in range(total_len - 1 , -1 , -1):
            all_possibilities[i] = 1 + all_possibilities[i+1]

            for word in dictionary:
                if i + len(word) <= total_len and s[i:i+len(word)] == word:
                    all_possibilities[i] = min(all_possibilities[i], all_possibilities[i+len(word)])
                
        return all_possibilities[0]



    
def main() -> None:
    sol = Solution()
    s: str = "sayhelloworld"
    dictionary: list[str] = ["hello","world"]
    result: int = sol.minExtraChar(s, dictionary)
    print(result)

    

if __name__ == "__main__":
    main()