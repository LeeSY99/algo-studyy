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

for start, end_list in edges.items():
    for end in end_list:
        in_count[end] += 1

for node, count in in_count.items():
    if count == 0:
        root = node

visited = {node:0 for node in nodes}
def bfs(x):
    next_node = edges[x]
    for y in next_node:
        visited[y] +=1
        bfs(y)
        

# print(in_count)
# print(root)
visited[root] = 1
bfs(root)
ans = 1
# print(visited)
for node, is_visited in visited.items():
    if is_visited != 1:
        ans = 0
        break

print(ans)
