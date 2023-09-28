import copy
from sudoku.structure import Grid
from sudoku import display

class Solver:
    def __init__(self, grid=None, stack=[]):
        self.iterations = 0
        if not grid:
            self.grid = Grid()
        else:
            self.grid = grid
        self.stack = stack

    def done(self):
        for i in range(9):
            for j in range(9):
                if not self.grid[i][j].collapsed:
                    return False
        return True
    
    def _prep(self, puzzle):
        if not puzzle:
            return
        if type(puzzle) == str:
            i = 0
            for l in puzzle.split('\n'):
                if i < 9:
                    for j in range(9):
                        if l[j] in "123456789":
                            self.stack.append((i,j,int(l[j])))
                    i += 1
        else:
            for i in range(9):
                for j in range(9):
                    if puzzle[i][j] != 0:
                        self.stack.append((i,j,puzzle[i][j]))

    def _solve(self, grid, stack):
        self.iterations += 1
        while len(stack) > 0:
            row, col, num = stack.pop()
            stack += grid.propagate(row, col, num)
        # i,j = grid.find_next()
        # if i != None and j != None:
        #     for v in grid[i][j].values():
        #         new_grid = copy.deepcopy(grid)
        #         if self._solve(new_grid, [(i, j, v)]):
        #             return new_grid
        # elif grid.is_valid():
        #     return grid
        # return False

    def solve_puzzle(self, puzzle):
        self._prep(puzzle)
        res = self._solve(self.grid, self.stack)
        print(self.iterations)
        if res:
            self.grid = res
