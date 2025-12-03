from collections import deque
n,m1,m2 = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m1):
    a1, b1 = map(int, input().split())
    graph[a1].append(b1)
    indegree[b1] += 1

for _ in range(m2):
    a2, b2 = map(int, input().split())
    # graph[a1].append(b2)
    # graph[b2].append(a1)


q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

visited = [False] * (n+1)
while q:
    x = q.popleft()
    visited[x] = True
    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)

is_cycle = False
for i in range(1, n + 1):
    if not visited[i]: 
        is_cycle = True

if is_cycle:
    print("No")
else:
    print("Yes")

