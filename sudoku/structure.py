import math

class Cell:
    def __init__(self):
        self.collapsed = False
        self.state = 0b111111111

    def collapse(self, value=None, bit=None):
        if self.collapsed:
            return
        if value:
            num = 0b1 << value -1
        elif bit:
            num = bit
        mask = (0b1<<9) - 1 - num
        self.state &= mask 
        if self.state.bit_count() == 1:
            self.collapsed = True

    def __int__(self):
        return int(math.log2(self.state))+1
    
    def entropy(self):
        return self.state.bit_count()
    


class Grid:
    def __init__(self):
        self._grid = []
        for i in range(9):
            row = []
            for j in range(9):
                row += [Cell()]
            self._grid += [row]

    def __getitem__(self, i):
        return self._grid[i]
    
    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if not self._grid[i][j].collapsed:
                    return False
                
        return True

    def propagate(self, row, col, num):
        for q in range(9):
            if q != col:
                self._grid[row][q].collapse(num)
            if q != row:
                self._grid[q][col].collapse(num)
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if i != row and j != col:
                    self._grid[i][j].collapse(num)
