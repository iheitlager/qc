def display_grid(grid):
    for i in range(9):
        if i in [3, 6]:
            print ('------+-------+------')
        l = ""
        for j in range(9):
            l += str(grid[i][j])
            l += " | " if j in [2, 5] else " "
        print(l)

def display_superpositiongrid(grid):
    for i in range(9):
        if i in [3, 6]:
            print ('------------+-------------+------------')
        else:
            print ('            |             |            ')
        for row in range(0,3):
            l = ""
            for j in range(9):
                p = grid[i][j]
                for col in range(0,3): 
                    a = p & (0b1 << row*3+col)
                    l += str(int(math.log2(a))+1) if a != 0 else '.'
                l += ' '
                if j in (2,5):
                    l += '| '
            print(l)
    print("")