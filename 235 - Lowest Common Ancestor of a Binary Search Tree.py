from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> TreeNode:
        l1: list[TreeNode] = self.search(root, p, [])
        l2: list[TreeNode] = self.search(root, q, [])

        search: list[TreeNode] = []
        searched: list[TreeNode] = []
        if len(l1) > len(l2):
            search = l1
            searched = l2
        else:
            search = l2
            searched = l1

        for val in search[::-1]:
            if val in searched:
                return val

        return TreeNode(0)

    def search(
        self, node: Optional[TreeNode], target: Optional[TreeNode], path: list[TreeNode]
    ) -> list[TreeNode]:
        if not node or not target:
            return path

        path.append(node)

        if node.val == target.val:
            return path

        if target.val > node.val:
            return self.search(node.right, target, path)
        else:
            return self.search(node.left, target, path)
