# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = 0
        right = 0
        def traverse(node):
            if not node:
                return 0
            if node:
                right = 1 + traverse(node.right)
                left =  1 + traverse(node.left)
            return max(left, right)                 
        return traverse(root)

