# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(leftRoot, rightRoot):
            if not leftRoot and not rightRoot:
                return True
            elif leftRoot and rightRoot:
                if leftRoot.val != rightRoot.val:
                    return False
                else:
                   A = traverse(leftRoot.left, rightRoot.right)
                   B = traverse(rightRoot.right, leftRoot.left)
                   return A and B
        return traverse(root, root)


        