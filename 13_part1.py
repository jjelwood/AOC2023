input = open("13.txt").read()
test = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#\
"""

import numpy as np

#input = test
groups = [group.split("\n") for group in input.split("\n\n")]

def check_candidates(potential_rows, potential_cols, rows, cols):
    for i in potential_rows:
        if is_reflection(rows, i):
            return 100 * (i + 1)
    
    for i in potential_cols:
        if is_reflection(cols, i):
            return i + 1      

def is_reflection(items, i_left):
    d = 0
    while i_left + d + 1 < len(items) and i_left - d >= 0:
        if items[i_left + d + 1] != items[i_left - d]:
            return False
        d += 1
    
    return True

res = 0
for group in groups:
    columns = ["" for _ in range(len(group[0]))]
    potential_rows = []
    potential_cols = []

    for i, row in enumerate(group):
        for j, c in enumerate(row):
            columns[j] += c
        
        if i != len(group) - 1 and row == group[i+1]:
            potential_rows.append(i)

    for i, column in enumerate(columns):
        if i != len(columns) - 1 and column == columns[i+1]:
            potential_cols.append(i)

    score = check_candidates(potential_rows, potential_cols, group, columns)
    res += score

print(res)
    
