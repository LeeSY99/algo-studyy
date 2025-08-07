
import sys
import heapq
n,m = map(int, input().split())
k = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    tree[u].append((v,w))
    tree[v].append((u,w))


def djkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cur_dist, now = heapq.heappop(q)

        if cur_dist > dist[now]:
            continue

        for v, weight in tree[now]:
            next_dist = dist[now] + weight
            if next_dist < dist[v]:
                dist[v] = next_dist
                heapq.heappush(q, (next_dist, v))
    return dist

dist = djkstra(k)
for i in range(1,n+1):
    # if i == k:
    #     continue
    if dist[i] == sys.maxsize:
        print(-1)
    else:
        print(dist[i]) 
