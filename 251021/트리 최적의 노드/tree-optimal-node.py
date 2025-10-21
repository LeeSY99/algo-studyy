import sys
sys.setrecursionlimit(100000)
n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def search(x):
    global max_dist, max_node
    for y in edges[x]:
        if visited[y]: continue
        visited[y] = True
        dist[y] = dist[x] + 1
        # if dist[y] > max_dist:
        #     max_dist = dist[y]
        #     max_node = y
        search(y)


visited = [False] * (n+1)
visited[1] = True
dist = [0] * (n+1)
search(1)
# print(dist)

fatherest = 0
fatherest_node = None
for i in range(1,n+1):
    if dist[i] >  fatherest:
        fatherest = dist[i]
        fatherest_node = i

# print(fatherest_node)
visited = [False] * (n+1)
visited[fatherest_node] = True
dist = [0] * (n+1)
search(fatherest_node)
print((max(dist) + 1 )//2)


