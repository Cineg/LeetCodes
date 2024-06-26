# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr: list[int] = []
        self.inorder(root)

        return self.buildTree(0, len(self.arr) - 1)

    def inorder(self, node: TreeNode) -> None:
        if not node:
            return

        self.inorder(node.left)
        self.arr.append(node.val)
        self.inorder(node.right)

    def buildTree(self, l: int, r: int) -> TreeNode:
        if l > r:
            return

        mid: int = (l + r) // 2
        root: TreeNode = TreeNode(self.arr[mid])
        root.left = self.buildTree(l, mid - 1)
        root.right = self.buildTree(mid + 1, r)

        return root


def main():
    Tree = TreeNode(2, TreeNode(1), TreeNode(3))
    sol = Solution()
    res: TreeNode = sol.balanceBST(Tree)

    print(res)


if __name__ == "__main__":
    main()
