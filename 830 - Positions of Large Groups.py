class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result: list = []
        temp_item: list = []
        temp_letter: str = ""
        i: int = 0
        while i < len(s):
            if len(temp_item) != 0:
                if temp_letter != s[i]:
                    if (i-1) - temp_item[0] >= 2:
                        temp_item.append(i-1)
                        result.append(temp_item)
                    
                    temp_item = []
                
                elif i + 1 == len(s):
                    if i - temp_item[0] >= 2:
                        temp_item.append(i)
                        result.append(temp_item)


            if len(temp_item) == 0:
                temp_item.append(i)
                temp_letter = s[i]
            
            i += 1

        return result