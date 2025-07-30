n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

import sys
dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]

# for i in range(n):
#     dp[0][i] = sys.maxsize

dp[1][n-1] = grid[0][n-1]
for i in range(1,n+1):
    for j in range(n-1,-1,-1):
        if i==1 and j==n-1:
            continue
        dp[i][j] = min(dp[i][j+1], dp[i-1][j]) + grid[i-1][j]

# for d in dp:
#     print(*d)
print(dp[n][0])