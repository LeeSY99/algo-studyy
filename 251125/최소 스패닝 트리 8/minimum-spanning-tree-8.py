import heapq
n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,v = map(int, input().split())
    graph[a].append((b,v))
    graph[b].append((a,v))

def prim(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    q=[]
    q.append((0,start))

    while q:
        now_d, now_node = heapq.heappop(q)

        if dist[now_node] != now_d:
            continue

        for next_node, weight in graph[now_node]:
            next_d = now_d + weight
            if dist[next_node] > next_d:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))

    return dist

print(max(prim(1)[1:]))

    


