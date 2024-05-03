from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def walk(node: Optional[TreeNode]):
            if not node:
                return

            l: TreeNode | None = node.left
            r: TreeNode | None = node.right
            node.right = l
            node.left = r

            walk(l)
            walk(r)

        walk(root)
        return root
