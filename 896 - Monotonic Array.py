class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 0: return True
        
        i: int = 0
        asc: str | None = None

        while i < len(nums) - 1:
            if asc == None:
                if nums[i] > nums[i+1]: asc = "desc"
                if nums[i] < nums[i+1]: asc = "asc"
            elif asc == "asc" and nums[i] > nums[i+1]: return False
            elif asc == "desc" and  nums[i] < nums[i+1]: return False
            
            i += 1

        return True

def main() -> None:
    sol = Solution()
    print(sol.isMonotonic([2,1,3,7]))

if __name__ == "__main__":
    main()