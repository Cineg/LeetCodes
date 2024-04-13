from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.walk(root, -inf, inf)

    def walk(self, node: Optional[TreeNode], lo: int | float, hi: int | float) -> bool:
        if not node:
            return True

        if node.val <= lo or node.val >= hi:
            return False

        return self.walk(node.left, lo, node.val) and self.walk(
            node.right, node.val, hi
        )


def main():

    tree = TreeNode(0, None, TreeNode(-1))
    sol = Solution()
    res = sol.isValidBST(tree)
    print(res)


if __name__ == "__main__":
    main()
