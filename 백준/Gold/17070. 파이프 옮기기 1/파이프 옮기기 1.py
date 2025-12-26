n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            if j-1 >= 0:
                dp[i][j][0] += dp[i][j-1][0]
                dp[i][j][0] += dp[i][j-1][1]
            if i-1 >= 0:
                dp[i][j][2] += dp[i-1][j][2]
                dp[i][j][2] += dp[i-1][j][1]

        if grid[i][j] == 0 and grid[i-1][j] == 0 and grid[i][j-1] == 0:
            if j - 1 >= 0 and i - 1 >= 0:
                dp[i][j][1] += dp[i-1][j-1][0]
                dp[i][j][1] += dp[i - 1][j - 1][1]
                dp[i][j][1] += dp[i - 1][j - 1][2]
# for d in dp:
#     print(*d)
print(sum(dp[n-1][n-1]))