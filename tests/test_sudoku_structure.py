import unittest
from sudoku.structure import Cell, Grid

class CellTests(unittest.TestCase):
    def test_instantiation(self):
        c = Cell()
        self.assertTrue(int(c), 9)
        self.assertFalse(c.collapsed)
        self.assertTrue(c.entropy(), 9)

    def test_masking_value_range(self):
        c = Cell()
        for i in range(9,0,-1):
            c.collapse(value=i)
            self.assertTrue(int(c), i-1)
        self.assertTrue(c.entropy(), 1)
        self.assertTrue(int(c), 1)
        self.assertTrue(c.collapsed)

    def test_masking_bit_range(self):
        c = Cell()
        for i in range(9,0,-1):
            c.collapse(bit=0b1 << i-1)
            self.assertTrue(int(c), i-1)
        self.assertTrue(c.entropy(), 1)
        self.assertTrue(int(c), 1)
        self.assertTrue(c.collapsed)


class GridTests(unittest.TestCase):
    def test_instantiation(self):
        g = Grid()
        self.assertFalse(g.is_complete())

if __name__ == '__main__':
    unittest.main()