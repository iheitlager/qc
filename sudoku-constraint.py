# https://pypi.org/project/python-constraint/
# https://sonalake.com/latest/constraint-programming-solving-sudoku-with-choco-solver-library/

from constraint import * 

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

solution = problem.getSolution()
for i in range(9):
    line = []
    for j in range(9):
        line.append(solution[i*9+j])
    print(line)
