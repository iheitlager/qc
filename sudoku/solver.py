import copy
from sudoku.structure import Grid

class Solver:
    def __init__(self, grid=None, stack=[]):
        if not grid:
            self.grid = Grid()
        else:
            self.grid = grid
        self.stack = stack

    def done(self):
        for i in range(9):
            for j in range(9):
                if not self.grid[i][j].collapsed():
                    return False
        return True
    
    def _prep(self, puzzle):
        if not puzzle:
            return
        stack = []
        if type(puzzle) == str:
            i = 0
            for l in puzzle.split('\n'):
                for j in range(9):
                    stack.append((i,j,int(l[j])))
                i += 1
        else:
            for i in range(9):
                for j in range(9):
                    if puzzle[i][j] != 0:
                        self.stack.append((i,j,puzzle[i][j]))

    def solve_puzzle(self, puzzle):
        self._prep(puzzle)
        while self.stack:
            row, col, num = self.stack.pop()
            self.grid.propagate(row, col, num)