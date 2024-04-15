from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res: list[int] = self.walk(root, "", [])
        return sum(res)

    def walk(self, node: Optional[TreeNode], val: str, res: list[int]) -> list[int]:

        if not node:
            return res

        val += str(node.val)

        if node and not node.left and not node.right:
            res.append(int(val))
            return res

        self.walk(node.left, val, res)
        self.walk(node.right, val, res)

        return res


def main():
    sol = Solution()

    tree = TreeNode(1, TreeNode(2), TreeNode(3))

    sol.sumNumbers(tree)


if __name__ == "__main__":
    main()
