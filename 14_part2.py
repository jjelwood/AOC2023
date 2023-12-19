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
    return "\n".join("".join(row) for row in grid)

def roll(cycles, grid):
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
    
    return grid

def get_stress(grid, hashed):
    result = 0
    if hashed:
        grid = grid.split("\n")
    for i, row in enumerate(grid):
        for col in row:
            if col == "O":
                result += rows - i
    return result

grid = [list(line) for line in input.split("\n")]
rows = len(grid)
cols = len(grid[0])

previously_seen = {get_hash(grid)}
cycles = []
stresses = []

i = 0
total_cycles = 1000000000
while i < total_cycles:
    for j in range(4):
        grid = roll(j, grid)
    
    # print(f"Cycle {i+1}:")
    # for row in grid:
    #     print("".join(row))
    # print()
    
    hash = get_hash(grid)
    if hash not in previously_seen:
        previously_seen.add(hash)
        cycles.append(hash)
    else:
        for i, cycle in enumerate(cycles):
            if cycle == hash:
                cycle_cycle_start = i
        cycle_cycle_length = len(cycles) - cycle_cycle_start
        print(cycle_cycle_start)
        print(cycle_cycle_length)
        grid = cycles[cycle_cycle_start + (total_cycles - cycle_cycle_start - 1) % cycle_cycle_length]
        break
    stresses.append(get_stress(grid, False))
    i += 1

result = 0

# for row in grid.split("\n"):
#     print("".join(row))

print([str(i) for i in stresses])
print([f"0{i}" for i in range(len(stresses))])
print(get_stress(grid, True))
