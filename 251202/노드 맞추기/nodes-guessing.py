n = int(input())
root = list(input().split())
m = int(input())
graph = {}
in_degree = {}

for _ in range(m):
    x,y = input().split()
    graph.setdefault(y, []).append(x)
    in_degree[x] = in_degree.get(x, 0) + 1

import heapq
q = []
for r in root:
    if in_degree.get(r, 0) == 0:
        heapq.heappush(q, r)

print(len(q))
print(*q)
tree = {}
while q:
    x = heapq.heappop(q)

    for y in graph.get(x, []):
        in_degree[y] -= 1
        if in_degree[y] == 0:
            heapq.heappush(q,y)
            tree.setdefault(x, []).append(y)

root.sort()
for r in root:
    children = sorted(tree.get(r, []))
    print(r, len(children), *children)


