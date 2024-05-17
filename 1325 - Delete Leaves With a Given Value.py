from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        dummy = TreeNode(target + 1)
        dummy.left = root

        self.walk(dummy.left, dummy, "l", target)
        return dummy.left

    def walk(
        self,
        node: Optional[TreeNode],
        parent: Optional[TreeNode],
        dir: str,
        target: int,
    ) -> None:
        if node == None:
            return

        self.walk(node.left, node, "l", target)
        self.walk(node.right, node, "r", target)

        if node.val == target and node.left == None and node.right == None:
            if dir == "l":
                parent.left = None
            if dir == "r":
                parent.right = None
