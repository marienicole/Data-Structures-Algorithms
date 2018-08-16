# Print a matrix spirally.
# Questions to ask:
#   1. Can I assume that the numbers are already in an array, or do I have to read them in?
#   2. Can I assume we're using the NumPy module?
#   3.
import numpy as np

matr = np.matrix([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

matr_list = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]

def print_spirally(matr):
    second = []
    rows, cols = matr.shape
    for r in range(0, rows):
            if (r%2 is not 0):
                for c in range(cols-1, -1, -1):
                    second.append(matr.item(r, c))
            else:
                for c in range(cols):
                    second.append(matr.item(r, c))

# printing as list instead of np matrix
def print_list_spirally(matrix):
    second = [0]
    cols = len(matrix)
    rows = len(matrix[0])
    for r in range(0, rows):
            if (r%2 is not 0):
                for c in range(cols-1, -1, -1):
                    second.append(matrix[r][c])
            else:
                for c in range(cols):
                    second.append(matrix[r][c])


print_list_spirally(matr_list)
