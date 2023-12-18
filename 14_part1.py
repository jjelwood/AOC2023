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

def roll_up(row, col):
    old_row = row
    while row != 0 and grid[row - 1][col] not in "#O":
        row -= 1
    grid[old_row][col] = "."
    grid[row][col] = "O"

def roll_down(row, col):
    old_row = row
    while row != rows - 1 and grid[row + 1][col] not in "#O":
        row += 1
    grid[old_row][col] = "."
    grid[row][col] = "O"

def roll_left(row, col):
    old_col = col
    while col != 0 and grid[row][col - 1] not in "#O":
        col -= 1
    grid[row][old_col] = "."
    grid[row][col] = "O"

def roll_right(row, col):
    old_col = col
    while col != cols - 1 and grid[row][col + 1] not in "#O":
        col += 1
    grid[row][old_col] = "."
    grid[row][col] = "O"

def get_hash(grid):
    return "".join("".join(row) for row in grid)

def roll(cycles):
    if cycles % 4 == 0:
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == "O":
                    roll_up(i, j)
    elif cycles % 4 == 1:
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == "O":
                    roll_left(i, j)
    elif cycles % 4 == 2:
        for i in range(len(grid) - 1, -1, -1):
            for j, col in enumerate(grid[i]):
                if col == "O":
                    roll_down(i, j)
    else:
        for i, row in enumerate(grid):
            for j in range(len(row) - 1, -1, -1):
                if row[j] == "O":
                    roll_right(i, j)


grid = [list(line) for line in test1.split("\n")]
rows = len(grid)
cols = len(grid[0])

previously_seen = {get_hash(grid)}
cycle_cycle = []

cycles = 0
while cycles < 10:
    for i in range(4):
        roll(i)
    
    print(f"Cycle {cycles+1}:")
    for row in grid:
        print("".join(row))
    print()
    
    # hash = get_hash(grid)
    # if hash not in previously_seen:
    #     previously_seen.add(hash)
    #     cycle_cycle.append(grid)
    # else:
    #     print(len(cycle_cycle))
    #     for c_grid in cycle_cycle:
    #         for row in c_grid:
    #             print("".join(row))
    #         print()
    #     grid = cycle_cycle[1000000000 % len(cycle_cycle)]
    #     break
    cycles += 1

result = 0

for row in grid:
    print("".join(row))

for i, row in enumerate(grid):
    for col in row:
        if col == "O":
            result += rows - i

print(result)
