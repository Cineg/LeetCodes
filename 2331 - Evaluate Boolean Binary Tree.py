from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.walk(root)

    def walk(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return False

        if node.val == 0:
            return False

        if node.val == 1:
            return True

        if node.val == 2:
            return self.walk(node.left) or self.walk(node.right)

        if node.val == 3:
            return self.walk(node.left) and self.walk(node.right)

        return True
