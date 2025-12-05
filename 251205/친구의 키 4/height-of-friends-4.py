n,m = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(m)]


indegree = [0] * (n+1)



from collections import deque

def is_cycle(limit):
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for i in range(limit):
        a,b = info[i]
        graph[a].append(b)
        indegree[b] += 1
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        visited[x] = True

        for y in graph[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)

    for i in range(1, n+1):
        if not visited[i]:
            return True
    return False

ans = 0
left,right = 0, m
while left<=right:
    mid = (left+right)//2
    if is_cycle(mid):
        right = mid-1
        ans = mid
    else:
        left = mid + 1

if ans == 0:
    print("Consistent")
else:
    print(ans)

    




