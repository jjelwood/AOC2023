input = open("14.txt").read()

test1 = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....\
"""

test2 = """\
#..
.O.
.#O
OOO\
"""

def get_stress(grid):
    result = 0
    
    for i, row in enumerate(grid):
        for col in row:
            if col == "O":
                result += rows - i
    return result

grid = [list(line) for line in input.split("\n")]
rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "O":
            old_row = row = i
            while row != 0 and grid[row - 1][j] not in "#O":
                row -= 1
            grid[old_row][j] = "."
            grid[row][j] = "O"

for row in grid:
    print("".join(row))

print(get_stress(grid))
