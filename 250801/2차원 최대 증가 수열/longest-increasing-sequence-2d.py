n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

for i in range(1,n):
    for j in range(1,m):
        for r in range(i):
            for c in range(j):
                if grid[r][c] < grid[i][j] and dp[r][c]!=0:
                    dp[i][j] = max(dp[i][j], dp[r][c]+1)


ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])
print(ans)

# for d in dp:
#     print(*d)