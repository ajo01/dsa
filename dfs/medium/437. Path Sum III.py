
class Solution:
    cnt = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(curr, start, currSum):
            if not curr:
                return
            currSum -= curr.val
            if currSum == 0:
                self.cnt += 1
            dfs(curr.left, False, currSum)
            dfs(curr.right, False, currSum)
            if start:
                dfs(curr.left, True, targetSum)
                dfs(curr.right, True, targetSum)
        dfs(root, True, targetSum)
        return self.cnt