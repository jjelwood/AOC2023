input = open("25.txt").read()
test ="""jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""

# input = test
lines = input.split("\n")

edges = {}
possible_breaks = []
for line in lines:
    info = line.split(":")
    for to in info[1].split():
        if info[0] not in edges:
            edges[info[0]] = {to}
        else:
            edges[info[0]].add(to)

        if to not in edges:
            edges[to] = {info[0]}
        else:
            edges[to].add(info[0])
        
        possible_breaks.append((info[0],to))

def get_groups(edges):
    nodes = set(edges)

    count = 0
    groups = []
    while nodes:
        count += 1

        if count > 2:
            return 3

        node = nodes.pop()

        queue = [node]
        visited = {node}
        while queue:
            node = queue.pop()
            for next_node in edges[node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)
                    nodes.remove(next_node)
        groups.append(visited)
    
    return groups

def remove_edge(edge):
    edges[edge[0]].remove(edge[1])
    edges[edge[1]].remove(edge[0])

def add_edge(edge):
    edges[edge[0]].add(edge[1])
    edges[edge[1]].add(edge[0])

def find_path(start, end):
    visited = {start}
    stack = [start]
    while stack:
        vertex = stack.pop(0)

        if vertex == end:
            return

        for next in edges[vertex]:
            if next in visited:
                continue

            edge_counts[tuple(sorted([vertex, next]))] += 1
            stack.append(next)
            visited.add(next)

edge_counts = {tuple(sorted(edge)): 0 for edge in possible_breaks}

import random

# vs = list(edges.keys())
# for i in range(10000):
#     # print(i)
#     start, end = random.sample(vs, 2)
#     # print(start, end)
#     find_path(start, end)

# print(sorted(((k, v) for k, v in edge_counts.items()), key=lambda x: x[1], reverse=True))

# These were the top 3 edges
edges_to_remove = [('jxb', 'ksq'), ('nqq', 'pxp'), ('dct', 'kns')]

for edge in edges_to_remove:
    remove_edge(edge)

groups = get_groups(edges)

print(len(groups[0]) * len(groups[1]))