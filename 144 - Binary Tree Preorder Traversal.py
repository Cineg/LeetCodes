from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res: list[int] = []

        def walk(node: Optional[TreeNode]):
            if node == None:
                return

            res.append(node.val)
            walk(node.left)
            walk(node.right)

        walk(root)
        return res
