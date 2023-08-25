class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    zero_pos.append([i,j])

        for k, l in zero_pos:
            for row in range(0, n):
                matrix[k][row] = 0
            for col in range(0, m):
                matrix[col][l] = 0
                