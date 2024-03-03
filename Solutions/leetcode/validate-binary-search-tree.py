# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, p, q):
            if not root:
                return True
            if not (root.val < q and root.val > p):
                return False
            left = isValid(root.left, p, root.val)
            right = isValid(root.right, root.val, q)
            return left and right
        return isValid(root, float("-inf"), float("inf"))