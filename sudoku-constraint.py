# https://pypi.org/project/python-constraint/
# https://sonalake.com/latest/constraint-programming-solving-sudoku-with-choco-solver-library/

from constraint import * 
import sys

def display_grid(solution):
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        l = ""
        for j in range(9):
            l += str(solution[i*9+j])
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

def solve(sudoku_grid):
    problem = Problem(BacktrackingSolver())
    for i in range(9):
        for j in range(9):
            if sudoku_grid[i][j] == 0:
                problem.addVariable(i*9+j, range(1,9+1))
            else:
                problem.addVariable(i*9+j, [sudoku_grid[i][j]])

    for row in range(9):
        # problem.addConstraint(ExactSumConstraint(45),[row*9+i for i in range(9)])
        problem.addConstraint(AllDifferentConstraint(),[row*9+i for i in range(9)])
    for col in range(9):
        # problem.addConstraint(ExactSumConstraint(45),[row+i*9 for i in range(9)])
        problem.addConstraint(AllDifferentConstraint(),[col+i*9 for i in range(9)])
    for row in range(0,9,3):
        for col in range(0,9,3):
            # problem.addConstraint(ExactSumConstraint(45),[(row+i)*9+col+j for i in range(3) for j in range(3)])
            problem.addConstraint(AllDifferentConstraint(),[(row+i)*9+col+j for i in range(3) for j in range(3)])

    return problem.getSolution()


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
    solution = solve(sudoku_grid)
    display_grid(solution)