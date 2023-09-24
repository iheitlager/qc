# https://saturncloud.io/blog/python-sudoku-wave-function-collapse-algorithm-implementation/
# https://www.youtube.com/watch?v=2SuvO4Gi7uY
import numpy as np
import random


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


def prep_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                grid[i][j] = 0b111111111
            else:
                grid[i][j] = 0b1 << (grid[i][j] - 1)

def collapse(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j].bit_count() == 1:
                num = grid[i][j]
                mask = (0b1<<9) - 1 - num
                for q in range(9):
                    if q != j:
                        grid[i][q] &= mask
                    if q != i:
                        grid[q][j] &= mask
                # start_i = (i // 3) * 3
                # start_j = (j // 3) * 3
                # for i2 in range(start_i, start_i + 3):
                #     for j2 in range(start_j, start_j + 3):
                #         print ("[{0},{1}]".format(i2,j2), end="")
                #         if i2 != i and j2 != j:
                #             grid[i2][j2] &= mask
                # print("")
 

def entropy(grid):
    for i in range(9):
        for j in range(9):
            grid[i][j] = grid[i][j].bit_count()

print(np.matrix(sudoku_grid))
prep_grid(sudoku_grid)
print(np.matrix(sudoku_grid))
collapse(sudoku_grid)
print(np.matrix(sudoku_grid))
entropy(sudoku_grid)
print(np.matrix(sudoku_grid))

