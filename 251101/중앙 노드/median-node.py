import sys
sys.setrecursionlimit(1000000)
n,r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

size = [0] * (n+1)

cent = 0
def cent_node(x):
    global cent
    visited[x] = True
    child = len(graph[x])
    if x != r:
        child -= 1
    
    if child >=2 and cent == 0:
        cent = x
    if child == 0 and cent == 0:
        cent = x

    for y in graph[x]:
        if visited[y]:
            continue
        cent_node(y)

def dfs(x):
    visited[x] = True
    size[x] = 1
    for y in graph[x]:
        if visited[y]:
            continue
        dfs(y)
        size[x] += size[y]

visited = [False] *(n+1)
cent_node(r)

visited = [False] *(n+1)
dfs(cent)

max_size, min_size = 0, n
for y in graph[cent]:
    max_size = max(max_size, size[y])
    min_size = min(min_size, size[y])
# print(size)
# print(max_size , min_size)
print(max_size - min_size)