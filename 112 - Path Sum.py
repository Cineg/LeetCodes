from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.walk(root, targetSum, 0, None)

    def walk(
        self,
        curr: Optional[TreeNode],
        targetSum: int,
        current: int,
        prev: Optional[TreeNode],
    ) -> bool:
        if not curr:
            if not prev or not prev.left and not prev.right:
                return targetSum == current
            return False

        current += curr.val

        left = self.walk(curr.left, targetSum, current, curr)
        right = self.walk(curr.right, targetSum, current, curr)

        if left or right:
            return True

        return False
