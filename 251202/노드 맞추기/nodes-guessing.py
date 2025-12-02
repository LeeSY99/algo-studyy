n = int(input())
root = list(input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
name_to_id = {}
id_to_name = {}
root.sort()

for i in range(n):
    name_to_id[root[i]] = i
    id_to_name[i] = root[i]

for _ in range(m):
    x,y = input().split()
    x_id = name_to_id[x]
    y_id = name_to_id[y]
    graph[y_id].append(x_id)
    in_degree[x_id] += 1

import heapq
q = []
for r in root:
    r_id = name_to_id[r]
    if in_degree[r_id]==0:
        heapq.heappush(q, r_id)

print(len(q))
for r in q:
    print(id_to_name[r], end = ' ')
print()
# print(graph)
tree = [[] for _ in range(n+1)]
while q:
    x_id = heapq.heappop(q)

    for y_id in graph[x_id]:
        in_degree[y_id] -= 1
        if in_degree[y_id] == 0:
            heapq.heappush(q, y_id)
            tree[x_id].append(y_id)


for r in root:
    r_id = name_to_id[r]
    children = sorted(tree[r_id])
    print(r, end = ' ')
    print(len(children), end = ' ')
    for c_id in children:
        print(id_to_name[c_id], end = ' ')
    print()


