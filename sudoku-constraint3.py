# https://gist.github.com/Tarliton/0620941c4383085d8ebf10bcf115e0e4
from collections import defaultdict
from constraint import *

example = """.......92
...1...4.
9..24...7
8..7..15.
65.9.1.78
.74..8..6
3...95..1
.8...6...
79.......
"""

example = """.3..78...
....5.3..
6.2..1.7.
7.....12.
.5.....3.
.91.....6
.4.8..6.7
..7.4....
...73..5.
"""

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

variables_with_value = {}
for i, line in enumerate(example.splitlines()):
    for j, val in enumerate(line):
        if val != '.':
            variables_with_value[f'm{i}{j}'] = int(val)

problem = Problem()
variables = []
groups = []
lines = defaultdict(list)
columns = defaultdict(list)
for q in range(3):
    for k in range(3):
        group = []
        for i in range(3):
            for j in range(3):
                var = f'm{(q*3)+i}{(k*3)+j}'
                variables.append(var)
                group.append(var)
                lines[f'{q*3 + i}'].append(var)
                columns[f'{k*3 + j}'].append(var)
        groups.append(group)
        
variables_pos = {v: i for i, v in enumerate(variables)}
print(variables)
for v in variables:
    value = variables_with_value.get(v)
    if value is None:
        problem.addVariable(v, range(1, 10))
    else:
        problem.addVariable(v, [value])
print(lines)
print(columns)
print(groups)
for group in groups:
    problem.addConstraint(AllDifferentConstraint(), group)
for _, line in lines.items():
    problem.addConstraint(AllDifferentConstraint(), line)
for _, column in columns.items():
    problem.addConstraint(AllDifferentConstraint(), column)

solution = problem.getSolution()

for i in range(9):
    line = []
    for j in range(9):
        line.append(solution[f'm{i}{j}'])
    print(line)