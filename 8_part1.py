input = open("8.txt").read()
test1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)\
"""
test2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)\
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

cur_node = "AAA"
end_node = "ZZZ"
steps = 0
directions_size = len(directions)
while cur_node != end_node:
    node = nodes[cur_node]
    if directions[steps % directions_size] == "R":
        cur_node = node.right
    else:
        cur_node = node.left
    steps += 1

print(steps)