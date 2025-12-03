n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

from collections import deque
q = deque()
count = 0
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        count += 1

while q:
    x = q.popleft()

    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)
            count += 1
# print(count)
if count != n:
    print("Exists")
else:
    print("Not Exists")
