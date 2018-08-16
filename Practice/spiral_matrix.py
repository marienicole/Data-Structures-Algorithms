
import numpy as np

matr = np.matrix([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

matr_list = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]

# we want to move right, then down, then left, then up
def print_matrix(matrix):
        if matrix == []:
            return matrix

        spiral = []
        rows = len(matrix)
        cols = len(matrix[0])

        m, n = 0, 0

        # m = left
        # n = top
        while m < rows and n < cols:
            for i in range(n, cols):
                spiral.append(matrix[m][i])
            m += 1


            for i in range(m, rows):
                spiral.append(matrix[i][cols-1])
            cols -= 1

            if (m < rows):
                for i in range(cols - 1, n - 1, -1):
                    spiral.append(matrix[rows-1][i])
                rows -= 1

            if (n < cols):
                for i in range(rows - 1, m - 1, -1):
                    spiral.append(matrix[i][n])
                n += 1

        return spiral

print(str(print_matrix(matr_list)))
