# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res: list[int] = []
        self.get_data(root, res)
        return res

    def get_data(self, root, res):

        if root:
            self.get_data(root.left, res)
            res.append(root.val)
            self.get_data(root.right, res)
