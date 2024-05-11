# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res: list[int] = []
        levels: set[int] = set()
        q: deque = deque()
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if node == None:
                continue

            if level not in levels:
                res.append(node.val)
                levels.add(level)

            q.append((node.right, level + 1))
            q.append((node.left, level + 1))

        return res
