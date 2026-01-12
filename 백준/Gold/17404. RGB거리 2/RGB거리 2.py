n = int(input())

cost = [[0,0,0]] + [list(map(int, input().split())) for _ in range(n)]

#dp[i][c] i번 째 집에 c색깔을 칠했을 떄 최소비용


ans = float('inf')
for c in range(3):
    dp = [[float('inf')] * 3 for _ in range(n + 1)]
    dp[1][c] = cost[1][c]
    for i in range(2, n+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    for j in range(3):
        if c == j:
            continue
        ans = min(ans, dp[n][j])

    # print(dp)
print(ans)
