import unittest
from sudoku.solver import Solver
from sudoku import display

example = """.6....19.
..261...4
7.1......
....7..1.
..6.83...
54..6...3
.8..27.39
...4...78
......4..
"""


class SolverTests(unittest.TestCase):
    def test_instantiation(self):
        s = Solver()
        self.assertFalse(s.done())


    def test_solver(self):
        s = Solver()
        s.solve_puzzle(example)

if __name__ == '__main__':
    unittest.main()