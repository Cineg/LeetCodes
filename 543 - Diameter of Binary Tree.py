from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def walk(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left: int = walk(node.left)
            right: int = walk(node.right)

            self.diameter = max(left + right, self.diameter)
            return 1 + max(left, right)

        walk(root)
        return self.diameter


def main():
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right = TreeNode(3)

    sol = Solution()
    res: int = sol.diameterOfBinaryTree(head)
    print(res)


if __name__ == "__main__":
    main()
