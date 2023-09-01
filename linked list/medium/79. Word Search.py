class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        boardDict = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDict[board[i][j]] +=1
        
        # key-letter, val-count
        wordDict = Counter(word)
        for letterCount in wordDict: 
            if letterCount not in boardDict or boardDict[letterCount] < wordDict[letterCount]:
                return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, 0, board, word):
                    return True
    
    def dfs(self, i, j, k, board, word):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or k>= len(word) or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True
        
        directions = [(1, 0),(-1,0), (0,1), (0, -1)]

        for x, y in directions:
            tmp = board[i][j]
            board[i][j] = -1
            if self.dfs(i+x, j+y, k+1, board, word):
                return True
            board[i][j] = tmp