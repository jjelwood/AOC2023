input = open("23.txt").read()
test = """#.#####################
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
#####################.#"""

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
    def __init__(self):
        self.visited = {1}
        self.heads = [1]
        self.head = 1
        self.length = 0
    
    def add(self, location):
        self.visited.add(location)
        self.head = location
        self.heads.append(location)
        self.length += 1
    
    def copy(self):
        new_path = Path()
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
    
    def get_nexts(self):
        if self.head == 1:
            return {1 + X}

        if island[self.head] == ">":
            if self.head + 1 not in self.visited:
                return {self.head + 1}
            return set()
        if island[self.head] == "<":
            if self.head - 1 not in self.visited:
                return {self.head - 1}
            return set()
        if island[self.head] == "v":
            if self.head + X not in self.visited:
                return {self.head + X}
            return set()
        if island[self.head] == "^":
            if self.head - X not in self.visited:
                return {self.head - X}
            return set()
        
        res = set()
        for dir in [1, -1, X, -X]:
            c = island[self.head + dir]
            if c != "#" and self.head + dir not in self.visited:
                res.add(self.head + dir)
        return res

    def vizualize(self):
        for l, c in enumerate(island):
            if l in self.visited:
                print("O", end="")
            else:
                print(c, end="")
            if l % X == X - 1:
                print()

def find_longest_path(path):
    if path.head == X * Y - 2:
        return path.length
    
    longest_path = 0
    for next in path.get_nexts():
        path.add(next)
        longest_path = max(longest_path, find_longest_path(path))
        path.go_back()
    return longest_path

path = Path()

import sys
sys.setrecursionlimit(3449)
print(find_longest_path(path))

