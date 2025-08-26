n,m = map(int, input().split())


# dp[i][j] : i번째 층 까지 고려, 마지막 들어간 방이 j

dp = [[0] * (m) for _ in range(n+1)] 
castle = [[0]*m] + [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(m):
        for k in range(m):#직전 층
            if j==k:
                continue

            dp[i][j] = max(dp[i][j], dp[i-1][k] + castle[i][j])

print(max(dp[n]))