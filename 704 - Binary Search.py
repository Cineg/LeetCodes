class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.walk(nums, target, 0, len(nums) - 1)

    def walk(self, arr: list[int], target: int, left: int, right: int) -> int:
        if left >= right:
            if target == arr[left]:
                return left
            else:
                return -1

        pivot: int = left + (right - left) // 2
        if arr[pivot] == target:
            return pivot

        if arr[pivot] > target:
            return self.walk(arr, target, left, pivot)
        else:
            return self.walk(arr, target, pivot + 1, right)


if __name__ == "__main__":
    sol = Solution()
    sol.search([-1, 0, 3, 5, 9, 12], 9)
