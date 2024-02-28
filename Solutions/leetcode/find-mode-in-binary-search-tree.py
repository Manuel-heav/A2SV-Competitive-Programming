# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        answer  = []
        item_dict = defaultdict(int)
        def traverse(node):
            if node:
                item_dict[node.val] += 1
                traverse(node.right)
                traverse(node.left)
        traverse(root)

        max_mode = max(item_dict.values())
        for keys, values in item_dict.items():
            if values == max_mode:
                answer.append(keys)
        return answer
        