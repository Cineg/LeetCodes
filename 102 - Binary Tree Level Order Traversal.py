from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:

        res: list[list[int]] = []

        if not root:
            return res

        q: list[list[Optional[TreeNode]]] = [[root]]

        while q:
            level: list[TreeNode | None] = q.pop()

            level_res: list[int] = []
            level_q: list[Optional[TreeNode]] = []
            for node in level:
                if node:
                    level_res.append(node.val)
                    level_q.append(node.left)
                    level_q.append(node.right)

            if len(level_q) > 0:
                q.append(level_q)
                res.append(level_res)

        return res
