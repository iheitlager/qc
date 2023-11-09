#!/usr/bin/env python
# https://www.adrian.idv.hk/2019-01-30-simanneal/


import copy
import random
import sys
from simanneal import Annealer

# from https://neos-guide.org/content/sudoku
_ = 0
PROBLEM = [
    1, _, _,  _, _, 6,  3, _, 8,
    _, _, 2,  3, _, _,  _, 9, _,
    _, _, _,  _, _, _,  7, 1, 6,

    7, _, 8,  9, 4, _,  _, _, 2,
    _, _, 4,  _, _, _,  9, _, _,
    9, _, _,  _, 2, 5,  1, _, 4,

    6, 2, 9,  _, _, _,  _, _, _,
    _, 4, _,  _, _, 7,  6, _, _,
    5, _, 7,  6, _, _,  _, _, 3,
]

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

def print_sudoku(state):
    border = "------+------+------"
    rows = [state[i:i+9] for i in range(0,81,9)]
    for i,row in enumerate(rows):
        if i % 3 == 0:
            print(border)
        three = [row[i:i+3] for i in range(0,9,3)]
        print(" |".join(
            " ".join(str(x or "_") for x in one)
            for one in three
        ))
    print(border)

def init_solution_row(problem):
    """Generate a random solution from a Sudoku problem
    """
    solution = []
    for i in range(0, 81, 9):
        row = problem[i:i+9]
        permu = [n for n in range(1,10) if n not in row]
        random.shuffle(permu)
        solution.extend([n or permu.pop() for n in row])
    return solution

def coord(row, col):
    return row*9 + col

class Sudoku_Row(Annealer):
    def __init__(self, problem):
        self.problem = problem
        state = init_solution_row(problem)
        super().__init__(state)
    def move(self):
        """randomly swap two cells in a random row"""
        row = random.randrange(9)
        coords = range(9*row, 9*(row+1))
        n1, n2 = random.sample([n for n in coords if self.problem[n] == 0], 2)
        self.state[n1], self.state[n2] = self.state[n2], self.state[n1]
    def energy(self):
        """calculate the number of violations: assume all rows are OK"""
        column_score = lambda n: -len(set(self.state[coord(i, n)] for i in range(9)))
        square_score = lambda n, m: -len(set(self.state[coord(3*n+i, 3*m+j)] for i in range(3) for j in range(3)))
        return sum(column_score(n) for n in range(9)) + sum(square_score(n,m) for n in range(3) for m in range(3))

def coord(row, col):
    return row*9+col

def main(problem):
    sudoku = Sudoku_Row(problem)
    sudoku.copy_strategy = "slice"
    sudoku.steps = 1000000
    print_sudoku(sudoku.state)
    state, e = sudoku.anneal()
    print("\n")
    print_sudoku(state)
    print(e)


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
    problem = []
    for l in sudoku_grid:
        problem += l
    main(problem)