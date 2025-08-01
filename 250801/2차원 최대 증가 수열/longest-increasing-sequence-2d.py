n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]


for i in range(1,n):
    for j in range(1,m):
        for r in range(i):
            for c in range(j):
                dp[i][j] = max(dp[i][j], dp[r][c]+1)

print(dp[n-1][m-1])
