n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
is_mini = [False] * (n+1)
dp = [[0] * (n+1) for _ in range(n+1)]
# dp[i][j] = i번 조각을 만드는데 필요한 j번 조각 개수

for _ in range(m):
    m_num, s_num, cnt = map(int, input().split())
    dp[m_num][s_num] = cnt
    graph[s_num].append((m_num, cnt))
    indegree[m_num] += 1
    
import heapq
q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
        is_mini[i] = True

while q:
    x = heapq.heappop(q)

    for y, cnt in graph[x]:
        indegree[y] -= 1
        for j in range(1,n+1):
            dp[y][j] += dp[x][j] * cnt

        if indegree[y] == 0:
            heapq.heappush(q, y)

# for d in dp:
#     print(*d)
for i in range(1, n+1):
    if is_mini[i]:
        print(i, dp[n][i])

