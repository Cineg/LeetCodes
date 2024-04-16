from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val, root)

        # parent, curr, depth
        q: list[tuple[Optional[TreeNode], Optional[TreeNode], int, str]] = [
            (None, root, 1, "")
        ]
        while q:
            parent, curr, c_depth, direction = q.pop(0)

            if c_depth == depth:
                if direction == "l":
                    node = TreeNode(val, curr)
                    parent.left = node

                if direction == "r":
                    node = TreeNode(val, None, curr)
                    parent.right = node
                continue

            if c_depth > depth:
                break

            if curr == None:
                continue

            q.append((curr, curr.left, c_depth + 1, "l"))
            q.append((curr, curr.right, c_depth + 1, "r"))

        return root
