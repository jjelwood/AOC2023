input = open("17.txt")
test = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533\
"""

test2 = """\
241
321
325\
"""

test3 = """\
11323
35623
54254
45452
67536
98454
87766
79653
86887
86453
65563
87735
55533\
"""

from queue import PriorityQueue
from functools import total_ordering

grid = [[int(cost) for cost in line] for line in test.split("\n")]
Y = len(grid)
X = len(grid[0])
nodes = {}

def hash(i, j):
    return X * i + j

class Node:
    def __init__(self, cost, location):
        self.cost = cost
        self.location = location
        self.vertical_neighbours = []
        self.horizontal_neighbours = []
    
    def get_neighbours(self):
        return self.vertical_neighbours + self.horizontal_neighbours
    
    def __str__(self):
        return f"Node(cost={self.cost}, location={self.location})"

@total_ordering
class Path:
    # Previous end location and end_location should both be hashes
    def __init__(self):
        self.node_locations = set()
        self.node_locations_list = []
        self.n_same_dir = 0
        self.total_cost = 0
        self.previous_end_location = -1
        self.end_location = -1
        self.has_done_3_in_a_row = False
    
    # Location should be a hash
    def add_node(self, location):
        if self.previous_end_location != -1 and self.end_location != -1:
            if self.end_location - self.previous_end_location != location - self.end_location:
                self.n_same_dir = 1
        self.previous_end_location = self.end_location
        self.end_location = location
        self.n_same_dir += 1
        self.node_locations.add(location)
        self.node_locations_list.append(location)
        self.total_cost += nodes[location].cost
        if self.n_same_dir >= 3:
            self.has_done_3_in_a_row = True
    
    def clone(self):
        new_path = Path()
        new_path.node_locations = self.node_locations.copy()
        new_path.node_locations_list = self.node_locations_list.copy()
        new_path.n_same_dir = self.n_same_dir
        new_path.total_cost = self.total_cost
        new_path.previous_end_location = self.previous_end_location
        new_path.end_location = self.end_location
        new_path.has_done_3_in_a_row = self.has_done_3_in_a_row
        return new_path
    
    def get_traversable_nodes(self):
        if self.n_same_dir < 3:
            return [node for node in nodes[self.end_location].get_neighbours() if node not in self.node_locations]
        
        return [node for node in nodes[self.end_location].get_neighbours() if node not in self.node_locations and
                 node - self.end_location != self.end_location - self.previous_end_location]
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    def __eq__(self, other):
        return self.total_cost == other.total_cost

    def summary(self):
        print("-----------------\nNodes:")
        for i, location in enumerate(self.node_locations_list):
            print(f"    {i+1}. {nodes[location]} {location}")
        print("Traversable Next Nodes:")
        for location in self.get_traversable_nodes():
            print(f"    {nodes[location]}")
        print(f"""\
End Location: {self.end_location}
Previous End Location: {self.previous_end_location}
Number in same Direction: {self.n_same_dir}
Total Cost: {self.total_cost}
-----------------""")

for i, row in enumerate(grid):
    for j, cost in enumerate(row):
        location = hash(i, j)
        new_node = Node(cost, location)
        if j != 0:
            new_node.horizontal_neighbours.append(location - 1)
        if j != X - 1:
            new_node.horizontal_neighbours.append(location + 1)
        if i != 0:
            new_node.vertical_neighbours.append(location - X)
        if i != Y - 1:
            new_node.vertical_neighbours.append(location + X)
        nodes[location] = new_node

def find_best_path():
    start = 0
    end = Y * X - 1

    default_path = Path()
    default_path.add_node(0)
    paths = PriorityQueue()
    paths.put((default_path.total_cost, default_path))
    paths_searched = 0
    longest_path_searched = 0

    nodes_reached_without_3_in_a_row = set()

    while not paths.empty():
        path = paths.get()[1]
        # path.summary()
        # print(f"Paths Searched: {paths_searched}")

        if len(path.node_locations) > longest_path_searched:
            longest_path_searched = len(path.node_locations)
            print(f"Searched a {longest_path_searched} length path after {paths_searched} iterations")

        if path.end_location == end:
            break

        for next_node in path.get_traversable_nodes():
            # if next_node not in nodes_reached_without_3_in_a_row:
            new_path = path.clone()
            new_path.add_node(next_node)
            paths.put((new_path.total_cost, new_path))
                # if not new_path.has_done_3_in_a_row:
                #     print(f"Number of nodes reached without three in a row: {len(nodes_reached_without_3_in_a_row)}")
                #     nodes_reached_without_3_in_a_row.add(next_node)
        
        paths_searched += 1
    else:
        print("No path found")

    path.summary()
    print(path.node_locations_list)
    print(start, end)

def testing():
    path = Path()
    path.add_node(0)
    path.add_node(1)
    path.add_node(2)
    path.summary()

find_best_path()
#testing()
