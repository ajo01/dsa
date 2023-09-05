class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                for x, y in directions: 
                    curX = i + x
                    curY = j + y
                    if (len(board) > curX and curX >= 0) and (len(board[0]) > curY and curY >= 0) and abs(board[curX][curY]) == 1:
                        live += 1

                if (live < 2 or live > 3) and board[i][j]:
                    board[i][j] = -1

                if not board[i][j] and live == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 1:
                    board[i][j] = 1
                if board[i][j] < 0:
                    board[i][j] = 0



class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copy_board = copy.deepcopy(board)
        directions = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                for x, y in directions: 
                    curX = i + x
                    curY = j + y
                    if (len(board) > curX and curX >= 0) and (len(board[0]) > curY and curY >= 0) and copy_board[curX][curY] == 1:
                        live += 1

                if (live < 2 or live > 3) and copy_board[i][j]:
                    board[i][j] = 0

                if not copy_board[i][j] and live == 3:
                    board[i][j] = 1


        
        