input = open("18.txt").read()

test ="""\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)\
"""

commands = input.split("\n")
location = (0, 0)
vertices = []
boundary_points = 0
for command in commands:
    params = command.split()
    if params[2][-2] == "1":
        dir = [0, 1]
    elif params[2][-2] == "3":
        dir = [0, -1]
    elif params[2][-2] == "2":
        dir = [-1, 0]
    elif params[2][-2] == "0":
        dir = [1, 0]
    
    n = int(params[2][2:-2], base=16)
    new_location = (location[0] + dir[0] * n, location[1] + dir[1] * n)
    boundary_points += n
    vertices.append(new_location)
    location = new_location

# Using the shoelace theorem
# However this doesn't count the edges of the shape, as each point is being measured with its area
area_excluding_edges = 1/2 * abs(sum(vertices[i][0] * (vertices[i - 1][1] - vertices[(i + 1) % len(vertices)][1]) for i in range(len(vertices))))

# Pick's Theorem
interior_points = area_excluding_edges - boundary_points / 2 + 1

print(interior_points + boundary_points)
