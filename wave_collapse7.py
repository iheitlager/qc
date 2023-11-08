# https://saturncloud.io/blog/python-sudoku-wave-function-collapse-algorithm-implementation/
# https://www.youtube.com/watch?v=2SuvO4Gi7uY
# https://www.boristhebrave.com/2020/04/13/wave-function-collapse-explained/

import numpy as np
import random
import sys
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
# sudoku_grid = [
#     [0, 6, 0, 0, 0, 0, 1, 9, 0],
#     [0, 0, 2, 6, 1, 0, 0, 0, 4],
#     [7, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 7, 0, 0, 1, 0],
#     [0, 0, 6, 0, 8, 3, 0, 0, 0],
#     [5, 4, 0, 0, 6, 0, 0, 0, 3],
#     [0, 8, 0, 0, 2, 7, 0, 3, 9],
#     [0, 0, 0, 4, 0, 0, 0, 7, 8],
#     [0, 0, 0, 0, 0, 0, 4, 0, 0]
# ]

def get_matrix(filename):
    """Return a list of lists containing the content of the input text file.

    Note: each line of the text file corresponds to a list. Each item in
    the list is from splitting the line of text by the whitespace ' '.
    """
    with open(filename, "r") as f:
        content = f.readlines()

    lines = []
    for line in content:
        new_line = line.rstrip()    # Strip any whitespace after last value

        if new_line:
            new_line = list(map(int, new_line.split(' ')))
            lines.append(new_line)

    return lines

    

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


def propagate_bitvalue(grid, stack):
    row, col, _n =stack.pop()
    num = 0b1 << _n -1
    mask = (0b1<<9) - 1 - num
    for q in range(9):
        if q != col and grid[row][q].bit_count() > 1 and grid[row][q] & num:
            grid[row][q] &= mask
            if grid[row][q].bit_count() == 1 and not grid[row][q] & num:
                stack.append((row, q, int(math.log2(grid[row][q]))+1))
        if q != row and grid[q][col].bit_count() > 1 and grid[q][col] & num:
            grid[q][col] &= mask
            if grid[q][col].bit_count() == 1 and not grid[q][col] & num:
                stack.append((q, col, int(math.log2(grid[q][col]))+1))
    start_i = (row // 3) * 3
    start_j = (col // 3) * 3
    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            if i != row and j != col and grid[i][j].bit_count() > 1  and grid[i][j] & num:
                grid[i][j] &= mask
                if grid[i][j].bit_count() == 1 and not grid[i][j] & num:
                    stack.append((i, j, int(math.log2(grid[i][j]))+1))
    grid[row][col] = num

def find_candidate(grid):
    # find first candidate bottom left to top right
    for entropy in range(2,10):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return None, None
                elif grid[i][j].bit_count() == entropy:
                    return i,j
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

def iter_positions(snum):
    for i in range(9,0, -1):
        if snum & 0b1 << i:
            yield i+1

def is_complete(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col].bit_count() > 1 or grid[row][col].bit_count() == 0:
                return False
    return True

def solve_sudoku(sgrid, stack=[]):
    global iterations
    iterations += 1
    while True:
        while len(stack):
            propagate_bitvalue(sgrid, stack)
        if is_complete(sgrid):
            return True
        row, col = find_candidate(sgrid)
        if row == None and col == None:
            return False
        for n in iter_positions(sgrid[row][col]):
            # print("Backtrack (%d,%d) = %d" % (row, col, n))
            new_grid = copy.deepcopy(sgrid)
            if solve_sudoku(new_grid, stack=[(row, col, n)]):
                for i in range(9):
                    for j in range(9):
                        sgrid[i][j]=new_grid[i][j]                
                return True
            else:
                return False
        return False


if __name__ == "__main__":
    # Read user input
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "problem.txt"
        print("Warning: using default problem file, '{}'. Usage: python "
              "{} <sudoku filepath>".format(filename, sys.argv[0]))

    # Read sudoku problem as matrix
    sudoku_grid = get_matrix(filename)

    # print("Start grid")
    # display_grid(sudoku_grid)


    sg = fill_superposition_grid()
    # display_superpositiongrid(sg)
    solve_sudoku(sg, prep_stack(sudoku_grid))
    # display_superpositiongrid(sg)
    display_grid(observe_grid(sg))

    print('Iterations: %d' % iterations)
