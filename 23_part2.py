input = open("23.txt").read()
test = """\
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#\
"""

test2 = """\
#.####
#.>..#
#.##.#
#....#
####.#\
"""

# input = test
lines = input.split("\n")
Y = len(lines)
X = len(lines[0])
island = input.replace("\n", "")

class Path:
    def __init__(self, start):
        self.visited = {start}
        self.heads = [start]
        self.head = start
        self.length = 0
    
    def add(self, location):
        self.visited.add(location)
        self.head = location
        self.heads.append(location)
        self.length += 1
    
    def copy(self):
        new_path = Path(1)
        new_path.visited = self.visited.copy()
        new_path.heads = self.heads.copy()
        new_path.head = self.head
        new_path.length = self.length
        return new_path
    
    def go_back(self):
        self.visited.remove(self.head)
        self.heads.pop()
        self.head = self.heads[-1]
        self.length -= 1
    
    def get_nexts(self, use_edges=False):
        if self.head == 1:
            return {1 + X}
        
        if self.head == X * Y - 2:
            return {X * (Y - 1) - 2}

        # if island[self.head] == ">":
        #     if self.head + 1 not in self.visited:
        #         return {self.head + 1}
        #     return set()
        # if island[self.head] == "<":
        #     if self.head - 1 not in self.visited:
        #         return {self.head - 1}
        #     return set()
        # if island[self.head] == "v":
        #     if self.head + X not in self.visited:
        #         return {self.head + X}
        #     return set()
        # if island[self.head] == "^":
        #     if self.head - X not in self.visited:
        #         return {self.head - X}
        #     return set()
        
        res = set()
        for dir in [1, -1, X, -X]:
            c = island[self.head + dir]
            if c != "#" and self.head + dir not in self.visited:
                res.add(self.head + dir)
        return res

    # def vizualize(self):
    #     for l, c in enumerate(island):
    #         if l in self.visited:
    #             print("O", end="")
    #         else:
    #             print(c, end="")
    #         if l % X == X - 1:
    #             print()

forks = set()

for l, c in enumerate(island):
    if c == "#":
        continue

    n_neighbours = 0
    for d in [1, -1, X, -X]:
        if 0 <= (l + d) % X < X and 0 <= (l + d) // X < Y:
            if island[l + d] != "#":
                n_neighbours += 1
    if n_neighbours > 2 or l == 1 or l == X * Y - 2:
        forks.add(l)

edges = {i: set() for i in forks}

# Construct edges
for fork in forks:
    # Search out from fork to find the distance to the next forks
    paths = [Path(fork)]

    while paths:
        path = paths.pop()
        if path.head != fork and path.head in forks:
            edges[fork].add((path.head, path.length))
            continue
        
        for next in path.get_nexts():
            new_path = path.copy()
            new_path.add(next)
            paths.append(new_path)

print(edges)
import sys
sys.setrecursionlimit(3449)

def find_longest_path(cur_length):
    if path[-1] == X * Y - 2:
        return cur_length
    
    longest_path = 0
    for next, dist in edges[path[-1]]:
        if next not in path:
            path.append(next)
            visited.add(next)
            longest_path = max(longest_path, find_longest_path(cur_length + dist))
            visited.remove(next)
            path.pop()
    return longest_path

path = [1]
visited = {1}
print(find_longest_path(0))

