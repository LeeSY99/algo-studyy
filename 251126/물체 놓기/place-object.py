import heapq
n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[0][i] = int(input())
for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, input().split()))

def prim(start):
    visited = [False] * (n+1)
    dist = [float('inf')] * (n+1)
    total_cost = 0
    dist[start] = 0


    for i in range(n+1):
        min_index = -1
        for j in range(n+1):
            if visited[j]: continue

            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j
            
        visited[min_index] = True
        total_cost += dist[min_index]

        for j in range(1,n+1):
            dist[j] = min(dist[j], graph[min_index][j])
    
    return total_cost

print(prim(0))
    

        