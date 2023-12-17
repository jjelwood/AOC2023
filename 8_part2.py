input = open("8.txt").read()
test = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)\
"""

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

nodes = {}

directions, connections = input.split("\n\n")
connections = connections.split("\n")
print(connections)
for connection in connections:
    print(connection)
    info = connection.split()
    from_node, l_node, r_node = info[0], info[2][1:-1], info[3][:-1]
    nodes[from_node] = Node(l_node, r_node)

node_strings = [node for node in nodes if node.endswith("A")]
steps_to_repeat = []
directions_size = len(directions)
for node_string in node_strings:
    cur_node_string = node_string
    steps = 0
    while not cur_node_string.endswith("Z"):
        cur_node = nodes[cur_node_string]
        if directions[steps % directions_size] == "R":
            cur_node_string = cur_node.right
        else:
            cur_node_string = cur_node.left
        steps += 1
    steps_to_repeat.append(steps)

import math
print(math.lcm(*steps_to_repeat))