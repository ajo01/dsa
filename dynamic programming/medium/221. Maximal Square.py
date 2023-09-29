
# input
# 0 1 1 0 
# 0 1 1 1
# 0 1 0 0

# dp
# 0 0 0 0 0
# 0 0 1 1 0
# 0 0 1 2 1
# 0 0 1 0 0

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    max_side = max(max_side, dp[i+1][j+1])
        return max_side * max_side