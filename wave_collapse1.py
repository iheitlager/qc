# https://saturncloud.io/blog/python-sudoku-wave-function-collapse-algorithm-implementation/

import numpy as np
import sys

iterations = 0

def display_grid(grid):
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        l = ""
        for j in range(9):
            l += str(grid[i][j])
            l += " | " if j in [2, 5] else " "
        print(l)

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


def solve_sudoku(grid):
    global iterations
    iterations += 1

    if is_complete(grid):
        return True

    row, col = find_empty_cell(grid)
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            # print("Iteration: {0:d}".format(iterations))
            # print(np.matrix(grid))
            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def is_complete(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return True

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

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

    print("Fill before rate: {0:d}".format(np.count_nonzero(sudoku_grid)))
    solve_sudoku(sudoku_grid)
    fr = np.count_nonzero(sudoku_grid)
    frp = fr / 81 * 100.0
    print("Fill after rate: {0:d} ({1:0.0f}%)".format(fr, frp))
    print("Iterations: {0:d}".format(iterations))
    display_grid(sudoku_grid)