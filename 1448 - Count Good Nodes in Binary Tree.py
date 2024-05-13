from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.good_nodes: int = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.walk(root, root.val)
        return self.good_nodes

    def walk(self, node: Optional[TreeNode], local_max: int) -> None:
        if node == None:
            return

        if node.val >= local_max:
            self.good_nodes += 1

        self.walk(node.left, max(node.val, local_max))
        self.walk(node.right, max(node.val, local_max))
