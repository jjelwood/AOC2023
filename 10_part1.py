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

input = test3
lines = input.split("\n")
X, Y = len(lines[0]), len(lines)
maze = input.replace("\n", "")

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
visited = 0
while current_tile != S:
    visited += 1
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

import math
print(math.ceil(visited / 2))