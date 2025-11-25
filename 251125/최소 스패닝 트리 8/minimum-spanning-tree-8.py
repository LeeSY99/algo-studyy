import heapq
n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,v = map(int, input().split())
    graph[a].append((b,v))
    graph[b].append((a,v))

def prim(start):
    visited = [False] * (n + 1)
    q=[]
    q.append((0,start))
    total_cost = 0

    while q:
        w, now_node = heapq.heappop(q)

        if visited[now_node]:
            continue

        visited[now_node] = True
        total_cost += w

        for next_node, weight in graph[now_node]:
            if not visited[next_node]:
                heapq.heappush(q, (weight, next_node))
    return total_cost

print(prim(1))

    


