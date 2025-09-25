import heapq
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

A, B = map(int, input().split())


def dijkstra(start):
    dist = [float('inf')] *(n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    path = [0]*(n+1)

    while q:
        now_d, now_node = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue

        for next_node, weight in graph[now_node]:
            next_d = now_d + weight
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))
                path[next_node] = now_node

    return dist, path

dist, path = dijkstra(A)

print(dist[B])


x = B
v = [x]
while x != A:
    x = path[x]
    v.append(x)
# print(path)
print(*v[::-1])
