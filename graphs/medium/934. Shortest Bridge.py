class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        directions = [(1,0),(-1,0), (0,-1), (0,1)]

        def invalid(i, j):
            return i < 0 or j < 0 or i == N or j == N  or (i,j) in visit

        # find islands
        def dfs(i, j):
            if invalid(i, j) or not grid[i][j]:
                return
            visit.add((i,j))

            for x, y in directions:
                dfs(i + x, j + y)

        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for x, y in directions:
                        curX = r + x
                        curY = c + y
                        if invalid(curX, curY):
                            continue
                        if grid[curX][curY] == 1:
                            return res

                        visit.add((curX, curY))
                        q.append([curX, curY])

                res += 1


        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()