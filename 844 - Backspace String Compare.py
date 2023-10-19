class Solution:    
    def backspaceCompare(self, s: str, t: str) -> bool:
        if s == t:
            return True

        str1: str = self.updateString(s)
        str2: str = self.updateString(t)

        return str2 == str1

    def updateString(self, string) -> str:
        res: str = ""
        for i in range(0, len(string)):
            if string[i] == "#":
                if len(res) > 0:
                    res = res[:-1]
                else:
                    res = ""
            else:
                res += string[i]
        return res