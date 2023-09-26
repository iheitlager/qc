# https://saturncloud.io/blog/python-sudoku-wave-function-collapse-algorithm-implementation/
# https://www.youtube.com/watch?v=2SuvO4Gi7uY
# https://www.boristhebrave.com/2020/04/13/wave-function-collapse-explained/

import numpy as np
import random
import math
import copy

iterations = 0

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


def display_grid(grid):
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        l = ""
        for j in range(9):
            l += str(grid[i][j])
            l += " | " if j in [2, 5] else " "
        print(l)

def display_superpositiongrid(grid):
    for i in range(9):
        if i in [3, 6]:
            print ('------------+-------------+------------')
        else:
            print ('            |             |            ')
        for row in range(0,3):
            l = ""
            for j in range(9):
                p = grid[i][j]
                for col in range(0,3): 
                    a = p & (0b1 << row*3+col)
                    l += str(int(math.log2(a))+1) if a != 0 else '.'
                l += ' '
                if j in (2,5):
                    l += '| '
            print(l)
    print("")

def prep_stack(grid):
    stack = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                stack.append((i,j,grid[i][j]))
    return stack

# we alter from positional grid with unknowns to superposition grid
def fill_superposition_grid():
    new_grid = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_row += [0b111111111] # nine digit super position
        new_grid.append(new_row)
    return new_grid

# we alter from positional grid with unknowns to superposition grid
def superposition_grid(grid):
    new_grid = []
    for i in range(9):
        new_row = []
        for j in range(9):
            # empty is all
            if grid[i][j] == 0:
                new_row += [0b111111111] # nine digit super position
            else:
                new_row += [0b1 << (grid[i][j] - 1)]
        new_grid.append(new_row)
    return new_grid

# we observe the grid and collapse to knows/unknowns
# note that if the grid is not solved, we introduce "errors"
def observe_grid(grid):
    new_grid = []
    for i in range(9):
        new_row = []
        for j in range(9):
            if grid[i][j] == 511:
                new_row += [0]
            else:
                new_row += [int(math.log2(grid[i][j]))+1]
        new_grid.append(new_row)
    return new_grid

# preparatory script to collapse superposition grid
def collapse_grid(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(9):
        for j in range(9):
            if grid[i][j].bit_count() == 1:
                propagate_bitvalue(new_grid, i, j, grid[i][j])
    return new_grid
 
def propagate_bitvalue(grid, stack):
    row, col, _n =stack.pop()
    num = 0b1 << _n -1
    mask = (0b1<<9) - 1 - num
    for q in range(9):
        if q != col and grid[row][q].bit_count() > 1 and grid[row][q] & num:
            grid[row][q] &= mask
            if grid[row][q].bit_count() == 1 and not grid[row][q] & num:
                stack.append((row, q, grid[row][q]))
        if q != row and grid[q][col].bit_count() > 1 and grid[q][col] & num:
            grid[q][col] &= mask
            if grid[q][col].bit_count() == 1 and not grid[q][col] & num:
                stack.append((q, col, grid[q][col]))
    start_i = (row // 3) * 3
    start_j = (col // 3) * 3
    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            if i != row and j != col and grid[i][j].bit_count() > 1  and grid[i][j] & num:
                grid[i][j] &= mask
                if grid[i][j].bit_count() == 1 and not grid[i][j] & num:
                    stack.append((i, j, grid[i][j]))
    grid[row][col] = num
    display_superpositiongrid(grid)

def calc_entropy(grid):
    new_grid = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_row += [grid[i][j].bit_count()]
        new_grid.append(new_row)
    return new_grid

def find_candidate(grid):
    # find first candidate bottom left to top right
    for entropy in range(2,10):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return None, None, -1
                elif grid[i][j].bit_count() == entropy:
                    return i,j, grid[i][j]
    return None, None, None


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

def iter_positions(snum):
    for i in range(9,0, -1):
        if snum & 0b1 << i:
            yield i+1

# def solve_sudoku(sgrid):
#     global iterations
#     iterations += 1

#     for entropy in range(1,10):
#         row, col = find_candidate(sgrid, entropy)
#         if row == None and col == None:
#             return True
#         else:
#             for num in iter_positions(sgrid[row][col]):
#                 new_grid = copy.deepcopy(sgrid)
#                 propagate_bitvalue(new_grid, row, col, 0b1 << num-1)
#                 if solve_sudoku(new_grid):
#                     for i in range(9):
#                         for j in range(9):
#                             sgrid[i][j] = new_grid[i][j]
#                     return True
#     return False

def solve_sudoku(sgrid, stack=[]):
    global iterations
    iterations += 1
    solved = False
    while not solved:
        while len(stack):
            propagate_bitvalue(sgrid, stack)
        row, col, num = find_candidate(sgrid)
        if num == -1:
            return False
        elif row == None and col == None:
            solved = True
        else:
            for n in iter_positions(num):
                new_grid = copy.deepcopy(sgrid)
                if solve_sudoku(new_grid, stack=[(row, col, n)]):
                    for i in range(9):
                        for j in range(9):
                            sgrid[i][j]=new_grid[i][j]
                    return True
    return True

print("Start grid")
display_grid(sudoku_grid)


sg = fill_superposition_grid()
display_superpositiongrid(sg)
solve_sudoku(sg, prep_stack(sudoku_grid))
display_superpositiongrid(sg)
display_grid(observe_grid(sg))
print("Entropy grid")
e = calc_entropy(sg)
display_grid(e)

# sg = superposition_grid(sudoku_grid)
# g2 = collapse_grid(sg)
# print(np.matrix(g2))
# # observe_grid(sudoku_grid)
# display_superpositiongrid(sg)
# # display_grid(observe_grid(sg))
# # print('')
# display_superpositiongrid(g2)
# # display_grid(observe_grid(g2))
# # print(np.matrix(sudoku_grid))
# print("Entropy grid")
# e = calc_entropy(g2)
# display_grid(e)

# print("Solution")
# if solve_sudoku(g2):
#     display_grid(observe_grid(g2))
# else:
#     print('No solution')
print('Iterations: %d' % iterations)
# # print(np.matrix(sudoku_grid))