from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(x):
    q = deque([(x,0)]) #(현재, 부모)
    while q:
        u,p = q.popleft()
        for v in graph[u]:
            if not visited[v]:
               visited[v] = True
               q.append((v,u))
            elif v != p:
                return True
    return False



ans = 0
for i in range(1,n+1):
    # print(i, visited)
    if not visited[i]:
        is_cycle = dfs(i)
        if not is_cycle:
            ans+=1

print(ans)