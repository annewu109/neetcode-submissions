class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in range(len(rows)):
            for length in range(len(matrix)):
                matrix[length][cols[i]] = 0
            for width in range(len(matrix[0])):
                matrix[rows[i]][width] = 0
        