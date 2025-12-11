import heapq

n,k = map(int, input().split())
MAX_N = 2*max(n, k)
dist = [float('inf')] * (MAX_N + 1)

dist[n] = 0
q = []
heapq.heappush(q, (0,n))

while q:
    now_d, now_node = heapq.heappop(q)

    if dist[now_node] != now_d:
        continue

    if 2*now_node <=MAX_N and dist[2*now_node] > dist[now_node]:
        dist[2*now_node] = dist[now_node]
        heapq.heappush(q, (now_d, 2*now_node))

    if now_node-1 >= 0 and dist[now_node-1] > dist[now_node]+1:
        dist[now_node-1] = dist[now_node] + 1
        heapq.heappush(q, (now_d+1, now_node-1))
    if now_node+1 <= MAX_N and dist[now_node+1] > dist[now_node]+1:
        dist[now_node+1] = dist[now_node]+1
        heapq.heappush(q, (now_d+1, now_node+1))


# print(*dist)
print(dist[k])

