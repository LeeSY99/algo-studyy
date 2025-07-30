n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]

# for d in dp:
#     print(*d)
print(dp[n][n])
