n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# i번 노드까지 고려
#dp[i][0] = i노드에 물건 놓지 않음
#dp[i][1] = i노드에 물건 놓음
dp = [[float('inf')]*(2) for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1
visited = [False] * (n+1)
for i in range(1,n+1):
    # for j in range(2):
    for next_node in graph[i]:
        #j==0
        dp[next_node][0] = min(dp[next_node][0], dp[i][1])
        #j==1
        dp[next_node][1] = min(dp[next_node][1], dp[i][0] + 1, dp[i][1]+1)


print(min(dp[n]))
