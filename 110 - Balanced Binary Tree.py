from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def walk(self, node: Optional[TreeNode]) -> int:

            if node == None:
                return 0

            left: int = walk(self, node.left)
            right: int = walk(self, node.right)

            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return walk(self, root) >= 0


def main() -> None:
    sol = Solution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(3)
    tree.left.left.left = TreeNode(4)
    tree.left.left.right = TreeNode(4)
    tree.right = TreeNode(2)

    res: bool = sol.isBalanced(tree)

    print(res)


if __name__ == "__main__":
    main()
