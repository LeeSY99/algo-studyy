n = int(input())
from collections import deque, defaultdict
graph = defaultdict(list)

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)
visited = [0] * (n+1)
queue = deque([1])
visited[1] = 1

while queue:
    now = queue.popleft()
    for next in graph[now]:
        if not visited[next]:
            visited[next] = 1
            parent[next] = now
            queue.append(next)

for i in range(2,n+1):
    print(parent[i])