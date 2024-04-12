# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.walk(root, 0)

    def walk(self, curr: Optional[TreeNode], depth: int) -> int:
        if not curr:
            return depth

        depth += 1

        return max(self.walk(curr.left, depth), self.walk(curr.right, depth))
