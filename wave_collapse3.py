# https://saturncloud.io/blog/python-sudoku-wave-function-collapse-algorithm-implementation/
# https://www.youtube.com/watch?v=2SuvO4Gi7uY
import numpy as np
import random

iterations = 0

def solve_sudoku(grid):
    global iterations
    iterations += 1

    row, col = find_empty_cell(grid)
    if row == None and col == None:
        return True  
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    # no more empty cell to be found, we are done
    return None, None

def is_valid(grid, row, col, num):
    # test rows and columns if num already exists
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # test adjecents if num already exists
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

#Example usage
# sudoku_grid = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# # Example usage
# sudoku_grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# Parool Wo 20 Sep ****
# sudoku_grid = [
#     [0, 0, 6, 0, 3, 0, 5, 2, 0],
#     [3, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 6, 4, 0, 0],
#     [5, 0, 0, 0, 0, 0, 0, 0, 6],
#     [0, 7, 0, 3, 5, 4, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 8, 4, 0],
#     [0, 0, 0, 2, 0, 0, 0, 0, 4],
#     [1, 0, 0, 0, 0, 7, 0, 9, 0],
#     [9, 5, 2, 0, 0, 0, 7, 0, 0]
# ]


# Parool 19 sept **
# sudoku_grid = [
#     [0, 0, 1, 0, 0, 3, 0, 6, 0],
#     [0, 4, 0, 6, 0, 0, 2, 0, 8],
#     [0, 3, 7, 0, 8, 2, 0, 0, 5],
#     [0, 0, 8, 0, 1, 0, 7, 0, 0],
#     [1, 0, 6, 7, 5, 0, 0, 0, 4],
#     [0, 9, 0, 0, 0, 8, 6, 0, 1],
#     [8, 0, 0, 2, 0, 0, 0, 4, 9],
#     [4, 0, 3, 1, 0, 5, 0, 2, 0],
#     [0, 1, 0, 0, 6, 0, 0, 0, 3]
# ]

# Parool Dinsdag 19 sept ****
sudoku_grid = [
    [0, 6, 0, 0, 0, 0, 1, 9, 0],
    [0, 0, 2, 6, 1, 0, 0, 0, 4],
    [7, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 1, 0],
    [0, 0, 6, 0, 8, 3, 0, 0, 0],
    [5, 4, 0, 0, 6, 0, 0, 0, 3],
    [0, 8, 0, 0, 2, 7, 0, 3, 9],
    [0, 0, 0, 4, 0, 0, 0, 7, 8],
    [0, 0, 0, 0, 0, 0, 4, 0, 0]
]
# sudoku_grid = [
#     [0, 6, 0, 0, 0, 0, 1, 9, 0],
#     [0, 0, 0, 6, 1, 0, 0, 0, 4],
#     [7, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 7, 0, 0, 1, 0],
#     [0, 0, 6, 0, 8, 3, 0, 0, 0],
#     [5, 4, 0, 0, 6, 0, 0, 0, 3],
#     [0, 8, 0, 0, 0, 7, 0, 3, 9],
#     [0, 0, 0, 4, 0, 0, 0, 7, 8],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

print("Fill before rate: {0:d}".format(np.count_nonzero(sudoku_grid)))
solve_sudoku(sudoku_grid)
fr = np.count_nonzero(sudoku_grid)
frp = fr / (9*9) * 100.0
print("Fill after rate: {0:d} ({1:0.0f}%)".format(fr, frp))
print("Iterations: {0:d}".format(iterations))
print(np.matrix(sudoku_grid))