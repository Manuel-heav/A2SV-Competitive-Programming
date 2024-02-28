# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        counter = 0
        def traverse(node):
            nonlocal counter
            if node:
                if node.val >= low and node.val <= high:
                    counter += node.val
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        return counter
        