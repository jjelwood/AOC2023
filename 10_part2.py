input = open("10.txt").read()
test1 = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ\
"""
test2 = """\
.....
.S-7.
.|.|.
.L-J.
.....\
"""
test3 = """\
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........\
"""
test4 = """\
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...\
"""


#input = test4
lines = input.split("\n")
X, Y = len(lines[0]), len(lines)
maze = input.replace("\n", "")

# def visualize(tile_coords):
#     grid = [list(line) for line in lines]
#     for tile in tile_coords:
#         grid[tile[1]][tile[0]] = "X"
#     for line in grid:
#         print("".join(line))

left_maps = {"-":-1, "L":-X, "F":X}
right_maps = {"-":1, "7":X, "J":-X}
up_maps = {"|":-X, "F":1, "7":-1}
down_maps = {"|":X, "L":1, "J":-1}

S = maze.find("S")

if S % X != 0 and maze[S - 1] in left_maps:
    loop_start = S - 1
elif S % X != X - 1 and maze[S + 1] in right_maps:
    loop_start = S + 1
elif S // Y != 0 and maze[S - X] in up_maps:
    loop_start = S - X
else:
    loop_start = S + X

previous_tile = S
current_tile = loop_start
loop = [S]
while current_tile != S:
    loop.append(current_tile)
    if current_tile == previous_tile + 1:       # travelled right
        offset = right_maps[maze[current_tile]]
    elif current_tile == previous_tile - 1:     # travelled left
        offset = left_maps[maze[current_tile]]
    elif current_tile == previous_tile - X:     # travelled up
        offset = up_maps[maze[current_tile]]
    else:                                       # travelled down
        offset = down_maps[maze[current_tile]]
    
    previous_tile = current_tile
    current_tile += offset

points = [(loop[i] % X, loop[i] // X) for i in range(len(loop))]

def is_in_loop(points, tile):
    winding_number = 0
    x, y = tile % X, tile // X + 0.1 # adding 0.1 to the y-coordinate to offset it from the edges
    for i in range(len(points)):
        a = points[i]
        b = points[(i + 1) % len(points)]

        pointA = (x - a[0], y - a[1])
        pointB = (x - b[0], y - b[1])

        if pointA[1] * pointB[1] < 0:
            r = pointA[0] + (pointA[1] * (pointB[0] - pointA[0])) / (pointA[1] - pointB[1])
            if r < 0:
                if pointA[1] < 0:
                    winding_number += 1
                else:
                    winding_number -= 1
    
    return int(winding_number % 2) == 1


result = 0
for tile in range(len(maze)):
    if tile in loop:
        continue
    if is_in_loop(points, tile):
        result += 1

print(result)

# import matplotlib.pyplot as plt

# coords = points
# coords.append(coords[0])

# xs, ys = zip(*coords)

# plt.figure()
# plt.plot(xs, ys)

# for tile in range(len(maze)):
#     if tile in loop:
#         continue
#     x, y = tile % X, tile // X
#     if is_in_loop(points, tile):
#         plt.plot(x, y, "go", markersize=1)
#     else:
#         plt.plot(x, y, "bo", markersize=1)

# plt.show()
