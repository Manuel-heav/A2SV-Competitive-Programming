# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        itemDict = defaultdict(list)
        count = 0
        def ziggy(node):
            nonlocal count
            if not node:
                return None
            if count % 2 == 0:
                itemDict[count].append(node.val)
            else:
                itemDict[count] = [node.val] + itemDict[count]
            count += 1
            left = ziggy(node.left)
            right = ziggy(node.right)
            count -= 1
        ziggy(root)
        return itemDict.values()
