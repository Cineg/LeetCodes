from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val: list[int] = []
        self.inorder(root, val)
        return val[k - 1]

    def inorder(self, node: Optional[TreeNode], values: list[int]):
        if node is None:
            return

        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)
