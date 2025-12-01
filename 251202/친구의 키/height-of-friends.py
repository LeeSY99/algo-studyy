from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1,n+1):
    if in_degree[i] == 0:
        q.append(i)

order = []
while q:
    now_node = q.popleft()
    order.append(now_node)
    for y in graph[now_node]:
        in_degree[y] -=1
        if in_degree[y] == 0:
            q.append(y)

print(*order)


