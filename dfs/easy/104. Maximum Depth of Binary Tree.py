# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 1

        if root.left and root.right:
            return depth + max(self.maxDepth(root.left), self.maxDepth(root.right))
        elif root.left:
            return depth + self.maxDepth(root.left)
        elif root.right:
            return depth + self.maxDepth(root.right)

        return depth