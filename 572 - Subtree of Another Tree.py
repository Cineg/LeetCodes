from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        if self.walk(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def walk(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if r and s:
            if r.val != s.val:
                return False

            return self.walk(r.left, s.left) and self.walk(r.right, s.right)

        return r == s


def main():
    sol = Solution()
    tree1 = TreeNode(3)
    tree1.left = TreeNode(4)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(2)
    tree1.right = TreeNode(5)

    tree2 = TreeNode(4)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(2)

    res = sol.isSubtree(tree1, tree2)
    print(res)


if __name__ == "__main__":
    main()
