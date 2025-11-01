import sys
sys.setrecursionlimit(100000)
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = [0] + list(map(int, input().split()))
for y in range(1,n+1):
    x = parent[y]
    if x == -1:
        continue
    graph[x].append(y)
    

score = [0] * (n+1)
for _ in range(m):
    i,w = map(int, input().split())
    score[i] +=  w
def dfs(x):
    for y in graph[x]:
        score[y] += score[x]
        dfs(y)
dfs(1)
print(*score[1:])