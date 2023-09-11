class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        dic: dict = {}
        for index, item in enumerate(groupSizes):
            if item in dic:
                dic[item].append(index)
            else:
                dic[item] = [index]

        solution: list[list[int]] = []
        for key in dic:
            loop: int = 0
            while loop < len(dic[key]):
                arr: list[int] = []
                for item in range(key):
                    arr.append(dic[key][item+loop])
                
                loop += key
                solution.append(arr)

        return solution

def main() -> None:
    sol = Solution()
    print(sol.groupThePeople([3,3,3,3,3,1,3]))

if __name__ == "__main__":
    main()