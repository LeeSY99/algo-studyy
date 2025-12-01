import heapq
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)


for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = []
for i in range(1,n+1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

order = []
while q:
    x = heapq.heappop(q)
    order.append(x)
    for y in graph[x]:
        in_degree[y] -= 1
        if in_degree[y] == 0:
            heapq.heappush(q, y)
            
print(*order)