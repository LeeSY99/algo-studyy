n = int(input())
edges = [[] for _ in range(n+1)]
import sys 
sys.setrecursionlimit(10000)

for _ in range(n-1):
    a,b,w = map(int, input().split())
    edges[a].append((b,w))
    edges[b].append((a,w))


dist = [0] * (n+1)

# start 에서 모든 접접 사이의 거리
def search(start, x):
    for y,d in edges[x]:
        if not visited[y]:
            visited[y] = True
            dist[y] = dist[x] + d
            search(start,y)

visited = [False] * (n+1)
visited[1] = True
search(1, 1)
fatherest = 0
fatherest_node = 0
for i in range(1,n+1):
    if dist[i] > fatherest:
        fatherest_node = i
        fatherest = dist[i]

dist = [0] * (n+1)
visited = [False] * (n+1)
visited[fatherest_node] = 1
search(fatherest_node, fatherest_node)
ans = max(dist)
# print(dist[fatherest_node])
print(ans)

