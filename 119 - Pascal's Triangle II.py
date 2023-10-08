class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle: list[list[int]] = self.generate(rowIndex + 1)
        return triangle[rowIndex]

    def generate(self, numRows: int) -> list[list[int]]:
        final_list: list = []
        for row in range(numRows):
            row_list = []

            if row == 1:
                row_list = [1,1]
                
            if row == 0:
                row_list = [1]

            if row > 1:
                row_list = [1]
                i = 1
                while i < len(final_list[row-1]):
                    value = final_list[row-1][i] + final_list[row-1][i-1]
                    row_list.append(value)
                    i += + 1

                row_list.append(1)

            final_list.append(row_list)
            
        return final_list
    

def main() -> None:
    sol = Solution()
    sol.getRow(1)


if __name__ == "__main__":
    main()