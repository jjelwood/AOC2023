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

def count_isolated_cycles(edges):
    nodes = set(edges)

    count = 0
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
    
    return count

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

def find_edges_and_get_groups():
    count = 0
    for i, edge1 in enumerate(possible_breaks):
        for j, edge2 in enumerate(possible_breaks[:i]):
            for edge3 in possible_breaks[:j]:
                count += 1
                if count % 100000 == 0:
                    print(count)
                for edge in [edge1, edge2, edge3]:
                    remove_edge(edge)
                if count_isolated_cycles(edges) == 2:
                    return get_groups(edges)
                for edge in [edge1, edge2, edge3]:
                    add_edge(edge)

print(len(possible_breaks))
groups = find_edges_and_get_groups()
res = 1
for group in groups:
    res *= len(group)
print(res)