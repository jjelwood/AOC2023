input = open("11.txt").read()
test = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....\
"""

# input = test
universe = input

universe = universe.split("\n")
expanded_rows = []
for i, row in enumerate(universe):
    expand_row = True
    for c in row:
        if c != ".":
            expand_row = False
            break
    if expand_row:
        expanded_rows.append(i)

expanded_cols = []
for i in range(len(universe[0])):
    expand_col = True
    for j in range(len(universe)):
        if universe[j][i] != ".":
            expand_col = False
            break
    if expand_col:
        expanded_cols.append(i)

def get_dist(x1, y1, x2, y2):
    dist = abs(x1 - x2) + abs(y1 - y2)
    for col in expanded_cols:
        if (col < x1) != (col < x2):
            dist += 1000000 - 1
    for row in expanded_rows:
        if (row < y1) != (row < y2):
            dist += 1000000 - 1
    return dist

galaxies = []
result = 0
pairs = 0
for i, row in enumerate(universe):
    for j, c in enumerate(row):
        if c == "#":
            for galaxy in galaxies:
                dist = get_dist(j, i, galaxy[0], galaxy[1])
                result += dist
                pairs += 1
            galaxies.append((j, i))

print(result)