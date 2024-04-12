# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        return self.walk(root, [])

    def walk(self, curr: Optional[TreeNode], arr: list[int]) -> list[int]:
        if not curr:
            return arr

        self.walk(curr.left, arr)
        arr.append(curr.val)
        self.walk(curr.right, arr)

        return arr
