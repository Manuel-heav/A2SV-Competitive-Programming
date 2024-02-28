# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node1, node2):
            new_Node = TreeNode()
            if not node1 and not node2:
                return None
            elif node1 and node2:
                new_Node.val = node1.val + node2.val
                new_Node.left = traverse(node1.left, node2.left)
                new_Node.right = traverse(node1.right, node2.right)
                return new_Node
            elif node1 and not node2:
                new_Node = node1
                return new_Node
            elif node2 and not node1:
                new_Node = node2
                return new_Node  
           
        return traverse(root1, root2) 


        