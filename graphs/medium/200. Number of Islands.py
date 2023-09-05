class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i, j):
            if i < 0 or j < 0 or i == M or j == N or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for x, y in directions:
                dfs(i+x, j+y)


        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res +=1
        return res