import math

class Cell:
    def __init__(self):
        self.collapsed = False
        self.state = 0b111111111

    def __int__(self):
        return int(math.log2(self.state))+1
    
    def __str__(self):
        return '<' + str(self.state) + '>'

    def collapse(self, value=None, bit=None):
        if self.collapsed:
            return False
        if value:
            num = 0b1 << value -1
        elif bit:
            num = bit
        mask = (0b1<<9) - 1 - num
        self.state &= mask 
        if self.state.bit_count() == 1:
            self.collapsed = True
        return self.collapsed

    def values(self):
        return [x for x in range(9) if self.state & 0b1 << x]
    
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
    
    def is_valid(self):
        for k in range(9):
            row = []
            for i in range(9):
                if self._grid[i][k].collapsed and int(self._grid[i][k]) not in row:
                    row.append(int(self._grid[i][k]))
            if len(row) != 9:
                return False
            col = []
            for j in range(9):
                if self._grid[k][j].collapsed and int(self._grid[k][j]) not in col:
                    col.append(int(self._grid[k][j]))
            if len(col) != 9:
                return False
        for row in range(0,9,3):
            for col in range(0,9,3):
                cell = []
                start_row = (row // 3) * 3
                start_col = (col // 3) * 3
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if self._grid[i][j].collapsed and int(self._grid[i][j]) not in cell:
                            cell.append(int(self._grid[i][j]))
                if len(cell) != 9:
                    return False
        return True
    
    def find_next(self):
        for e in range(2,10):
            for i in range(9):
                for j in range(9):
                    if self._grid[i][j].entropy() == e:
                        return (i,j)
        return (None, None)
    
    def propagate(self, row, col, num):
        self._grid[row][col].collapse(num)
        ret = []
        for q in range(9):
            if q != col:
                if self._grid[row][q].collapse(num):
                    ret += [(row, q, int(self._grid[row][q]))]
            if q != row:
                if self._grid[q][col].collapse(num):
                    ret += [(q, col, int(self._grid[q][col]))]
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if i != row and j != col:
                    if self._grid[i][j].collapse(num):
                        ret += [(i, j, int(self._grid[i][j]))]
        return ret