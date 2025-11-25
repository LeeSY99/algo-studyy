import heapq
n = int(input())

cost = [0] * (n)
for i in range(n):
    c = int(input())
    cost[i] = c

graph = [list(map(int, input().split())) for _ in range(n)]

def prim(start):
    visited = [False] * (n+1)
    dist = [float('inf')] * (n+1)
    total_cost = cost[start]
    dist[start] = 0


    for i in range(n):
        min_index = -1
        for j in range(n):
            if visited[j]: continue

            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j
            
        visited[min_index] = True
        total_cost += dist[min_index]

        for j in range(n):
            if graph[min_index][j] == 0:
                continue
            dist[j] = min(dist[j], graph[min_index][j])

    return total_cost

ans = float('inf')
for i in range(n):
    ans = min(ans, prim(i))
print(ans)
    

        