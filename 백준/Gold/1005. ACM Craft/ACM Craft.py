from collections import deque
T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    times = [0] + list(map(int, input().split()))
    for _ in range(k):
        x,y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    q = deque()
    res = [0] * (n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            res[i] = times[i]

    while q:
        x = q.popleft()
        for y in graph[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
            res[y] = max(res[y], res[x] + times[y])
    # print(*res)
    print(res[w])


