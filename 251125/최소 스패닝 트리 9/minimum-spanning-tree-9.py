import heapq
n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def prim(start):
    q = [(0,start)]
    visited = [False] * (n+1)
    cost = 0

    while q:
        w, node = heapq.heappop(q)

        if visited[node]: continue

        visited[node] = True
        cost += w

        for next_node, weight in graph[node]:
            if not visited[next_node]:
                heapq.heappush(q,(weight, next_node))

    return cost

print(prim(1))