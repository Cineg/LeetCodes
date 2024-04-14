from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 0

        return self.walk(root, None)

    def walk(
        self,
        curr: Optional[TreeNode],
        prev: Optional[TreeNode],
        curr_dir: str = "",
        prev_dir: str = "",
    ) -> int:
        if (
            curr_dir == "l"
            and (prev_dir == "l" or prev_dir == "")
            and not curr
            and not prev.right
        ):
            return prev.val

        elif not curr:
            return 0

        return self.walk(curr.left, curr, "l", curr_dir) + self.walk(
            curr.right, curr, "r", curr_dir
        )


def main():
    sol = Solution()

    tree = TreeNode(1, TreeNode(2))
    sol.sumOfLeftLeaves(tree)


if __name__ == "__main__":
    main()
