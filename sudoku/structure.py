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