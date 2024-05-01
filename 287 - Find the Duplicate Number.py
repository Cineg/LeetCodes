class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow: int = 0
        slow2: int = 0
        fast: int = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
