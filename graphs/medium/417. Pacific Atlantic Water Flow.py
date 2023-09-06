class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M = len(heights)
        N = len(heights[0])
        pacific = set()
        atlantic = set()



        def dfs(i, j, visit, prevHeight):
            if i < 0 or j < 0 or i == M or j == N or (i, j) in visit or heights[i][j] < prevHeight:
                return 
            visit.add((i, j))
            for x, y in directions:
                curX = i + x
                curY = j + y
                dfs(curX, curY, visit, heights[i][j])


        for i in range(M):
            dfs(i, 0, pacific, heights[i][0]) # left
            dfs(i, N - 1, atlantic, heights[i][N-1]) #right
        for i in range(N):
            dfs(0, i, pacific, heights[0][i]) #top
            dfs(M - 1, i, atlantic, heights[M-1][i]) # bt

        res = []
        for i in range(M):
            for j in range(N):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i,j])

        return res