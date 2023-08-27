# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = depth(node.left) if node.left else 0 
            right = depth(node.right) if node.right else 0
            if left + right > self.diameter:
                self.diameter = left + right 
            return 1 + max(left, right)
    

        depth(root)
        return self.diameter
    
