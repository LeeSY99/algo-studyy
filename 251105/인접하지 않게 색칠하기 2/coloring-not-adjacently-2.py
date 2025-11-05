n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
nums = [0] * (n+1)
for i in range(1,n+1):
    a = int(input())
    nums[i] = a
k = int(input())

#dp[i][j][0] : i노드 선택 안하고 총 j개 선택
#dp[i][j][1] : i노드 선택 하고 총 j개 선택
dp = [[[0]*2 for _ in range(k+1)] for _ in range(n+1)]

def dfs(x):
    visited[x] = True
    left = 0
    right = 0
    for j in range(1,k+1):
        dp[x][j][1] += nums[x]
    for y in graph[x]:
        if visited[y]: continue
        dfs(y)
        if left == 0:
            left = y
        else:
            right = y
    dp[x][1][1] = nums[x]
    dp[x][0][0] = 0
    #총 i개 색칠, 본 노드 색칠
    #왼쪽 j개 오른쪽 i-j-1개 그리고 본 노드 1개 -> 총 i개
    for i in range(1,k+1):
        for j in range(i):
            dp[x][i][1] = max(dp[x][i][1], dp[left][j][0] + dp[right][i-j-1][0] + nums[x])
    
    #총 i개 색칠, 본 노드 색칠 x
    #왼쪽 j개 오른쪽 i-j개 -> 총 i개
    for i in range(k+1):
        for j in range(i+1):
            dp[x][i][0] = max(dp[x][i][0], 
                max(dp[left][j][0] , dp[left][j][1]) + 
                max(dp[right][i-j][0], dp[right][i-j][1]))
        

visited = [False] * (n+1)
dfs(1)
ans = 0
for i in range(1,k+1):
    ans = max(ans, max(dp[1][i]))
print(ans)