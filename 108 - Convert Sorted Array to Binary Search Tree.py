# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        return self.walk(nums)

    def walk(self, nums: list[int]):
        if len(nums) == 0:
            return None

        mid: int = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.walk(nums[:mid])
        root.right = self.walk(nums[mid + 1 :])

        return root
