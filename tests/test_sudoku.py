import unittest
from sudoku.structure import Cell

class CellTests(unittest.TestCase):
    def test_instantiation(self):
        c = Cell()
        self.assertTrue(int(c), 9)


if __name__ == '__main__':
    unittest.main()