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
#....#..#

#..#.#........#
#..######..####
.##..#.#.##.#.#
#..##..........
######........#
#..####......##
.##.##.#...##.#\
"""

#input = test
groups = [group.split("\n") for group in input.split("\n\n")]

def check_candidates(potential_rows, potential_cols, rows, cols):
    for i in potential_rows:
        if is_reflection(rows, i):
            return 100 * (i + 1), f"r{i}"
    
    for i in potential_cols:
        if is_reflection(cols, i):
            return i + 1, f"c{i}"

    return 0  

def is_reflection(items, i_left):
    d = 0
    while i_left + d + 1 < len(items) and i_left - d >= 0:
        if items[i_left + d + 1] != items[i_left - d]:
            return False
        d += 1
    
    return True

def fix_smudge(group):
    old_score, ignore = find_reflection(group)
    for i, row in enumerate(group):
        for j, col in enumerate(row):
            group[i] = group[i][:j] + ("." if col == "#" else "#") + group[i][j+1:]
            score = find_reflection(group, ignore)
            group[i] = group[i][:j] + col + group[i][j+1:]
            if score != 0:
                return score

def find_reflection(group, ignore=""):
    columns = ["" for _ in range(len(group[0]))]
    potential_rows = []
    potential_cols = []

    for i, row in enumerate(group):
        for j, c in enumerate(row):
            columns[j] += c
        
        if ignore != f"r{i}" and i != len(group) - 1 and row == group[i+1]:
            potential_rows.append(i)

    for i, column in enumerate(columns):
        if ignore != f"c{i}" and i != len(columns) - 1 and column == columns[i+1]:
            potential_cols.append(i)

    return check_candidates(potential_rows, potential_cols, group, columns)

res = 0
for group in groups:
    score, _ = fix_smudge(group)
    res += score

print(res)
    
