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

    def test_values(self):
        c = Cell()
        self.assertTrue(c.values(), [1,2,3,4,5,6,7,8,9])
        c.collapse(3)
        self.assertTrue(c.values(), [1,2,4,5,6,7,8,9])
        c.collapse(5)
        self.assertTrue(c.values(), [1,2,4,6,7,8,9])
        c.collapse(8)
        self.assertTrue(c.values(), [1,2,4,5,6,7,9])


class GridTests(unittest.TestCase):
    def test_instantiation(self):
        g = Grid()
        self.assertFalse(g.is_complete())

if __name__ == '__main__':
    unittest.main()