input = open("17.txt").read()
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

from queue import PriorityQueue
from functools import total_ordering

grid = [[int(cost) for cost in line] for line in input.split("\n")]
Y = len(grid)
X = len(grid[0])
nodes = {}

class Node:
    def __init__(self, cost, location):
        self.cost = cost
        self.location = location
    
    def __str__(self):
        return f"Node(cost={self.cost}, location={self.location})"

@total_ordering
class Path:
    def __init__(self, start):
        self.total_cost = 0
        self.location = start
        self.n_same_dir = 0
        self.vel = 0
        self.length = 0
        self.nodes = [start] # Strictly for vizualising, not necessary for solving and would probably speed the program up if deleted
    
    def add_node(self, node):
        if node - self.location == self.vel:
            self.n_same_dir += 1
        else:
            self.n_same_dir = 1
        self.vel = node - self.location
        self.location = node
        self.total_cost += nodes[node].cost
        self.nodes.append(node)
        self.length += 1
    
    def clone(self):
        new_path = Path(self.location)
        new_path.vel = self.vel
        new_path.n_same_dir = self.n_same_dir
        new_path.total_cost = self.total_cost
        new_path.length = self.length
        new_path.nodes = self.nodes.copy()
        return new_path
    
    def get_traversable_nodes(self):
        res = []
        
        if self.n_same_dir < 4:
            if self.location % X != 0 and self.vel == -1:
                res.append(self.location - 1)
            if self.location % X != X - 1 and self.vel == 1:
                res.append(self.location + 1)
            if self.location // X != 0 and self.vel == -X:
                res.append(self.location - X)
            if self.location // X != Y - 1 and self.vel == X:
                res.append(self.location + X)
            
            # Starting case
            if self.vel == 0:
                res.append(self.location + 1)
                res.append(self.location + X)
            return res

        if self.n_same_dir >= 10:
            if self.location % X != 0 and abs(self.vel) != 1:
                res.append(self.location - 1)
            if self.location % X != X - 1 and abs(self.vel) != 1:
                res.append(self.location + 1)
            if self.location // X != 0 and abs(self.vel) != X:
                res.append(self.location - X)
            if self.location // X != Y - 1 and abs(self.vel) != X:
                res.append(self.location + X)
            return res
        
        if self.location % X != 0 and self.vel != 1:
            res.append(self.location - 1)
        if self.location % X != X - 1 and self.vel != -1:
            res.append(self.location + 1)
        if self.location // X != 0 and self.vel != X:
            res.append(self.location - X)
        if self.location // X != Y - 1 and self.vel != -X:
            res.append(self.location + X)
        return res
        

    def hash(self):
        return f"{self.location}, {self.vel}, {self.n_same_dir}"

    def vizualize_path(self):
        arrows = {}
        for i, node in enumerate(self.nodes):
            if i == 0:
                continue
            if node - self.nodes[i-1] == 1:
                arrows[node] = ">"
            elif node - self.nodes[i-1] == -1:
                arrows[node] = "<"
            elif node - self.nodes[i-1] == X:
                arrows[node] = "v"
            elif node - self.nodes[i-1] == -X:
                arrows[node] = "^"
            else:
                arrows[node] = "X"
        
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                l = X * i + j
                if l in arrows:
                    print(arrows[l], end="")
                else:
                    print(n, end="")
            print()

    
    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    def __eq__(self, other):
        return self.total_cost == other.total_cost

    def summary(self):
        print("Nodes:")
        for i, node in enumerate(self.nodes):
            print(f"    {i+1}. {nodes[node]}")
        print(f"""\
Length: {self.length}
Location: {self.location}
Velocity: {self.vel}
Number in same Direction: {self.n_same_dir}
Total Cost: {self.total_cost}
-----------------""")

for i, row in enumerate(grid):
    for j, cost in enumerate(row):
        location = X * i + j
        new_node = Node(cost, location)
        nodes[location] = new_node

def find_best_path():
    start = 0
    end = Y * X - 1

    default_path = Path(start)
    paths = PriorityQueue()
    paths.put(default_path)

    visited = set()

    while not paths.empty():
        path = paths.get()[1]

        if path.location == end:
            break

        for next_node in path.get_traversable_nodes():
            new_path = path.clone()
            new_path.add_node(next_node)
            hash = new_path.hash()
            if new_path.hash() not in visited:
                paths.put(new_path)
                visited.add(hash)
    else:
        print("No path found")

    path.summary()
    path.vizualize_path()
    print(path.total_cost)

find_best_path()