# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = [root, root]

        while q:
            l = q.pop(0)
            r = q.pop(0)

            if l and r:
                if l.val != r.val:
                    return False

                q.append(l.left)
                q.append(r.right)

                q.append(l.right)
                q.append(r.left)

            if not l and not r:
                continue

            if not l or not r:
                return False

        return True

        # return self.walk(root, root)

    def walk(self, left, right) -> bool:

        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.walk(left.left, right.right) and self.walk(left.right, right.left)
