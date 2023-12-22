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
edge_nodes = {location}
for command in commands:
    params = command.split()
    if params[0] == "D":
        dir = [0, 1]
    elif params[0] == "U":
        dir = [0, -1]
    elif params[0] == "L":
        dir = [-1, 0]
    elif params[0] == "R":
        dir = [1, 0]
    
    for _ in range(int(params[1])):
        new_location = (location[0] + dir[0], location[1] + dir[1])
        print(new_location)
        edge_nodes.add(new_location)
        location = new_location

# Guess that (1,1) is in the lagoon

inner_nodes = {(1,1)}
queue = [(1,1)]
while queue:
    node = queue.pop(0)

    for dir in [(0, 1), (0, -1), (1, 0), (-1,0)]:
        new_node = (node[0] + dir[0], node[1] + dir[1])
        if new_node not in inner_nodes and new_node not in edge_nodes:
            inner_nodes.add(new_node)
            queue.append(new_node)

print(len(inner_nodes) + len(edge_nodes))


#print(sorted(edge_nodes))
