from collections import defaultdict
m = int(input())
edges = defaultdict(list)
nodes = []
for _ in range(m):
    a,b = map(int, input().split())
    nodes.append(a)
    nodes.append(b)
    edges[a].append(b)

nodes = set(nodes)
nodes = sorted(nodes)
in_count = {node:0 for node in nodes}

visited = {node:0 for node in nodes}
def bfs(x):
    next_node = edges[x]
    for y in next_node:
        visited[y] +=1
        bfs(y)
        

# print(visited)
def check():
    root = None
    for start, end_list in edges.items():
        for end in end_list:
            in_count[end] += 1

    count = 0
    for node, count in in_count.items():
        if count == 0:
            count+= 1
            root = node
        if count > 1:
            return 0
    if count != 1:
        return 0

    # print(in_count)
    visited[root] = 1
    bfs(root)
    for node, visited_count in visited.items():
        if visited_count == 0:
            return 0
    return 1

print(check())
