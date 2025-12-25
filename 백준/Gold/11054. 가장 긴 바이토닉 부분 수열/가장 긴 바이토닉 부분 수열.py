n = int(input())
a = list(map(int, input().split()))

dp = [[1]*2 for _ in range(n)]
# dp[i][0] i에서 끝나고 증가중
# dp[i][1] i에서 끝나고 감소중

dp[0][0] = 1
dp[0][1] = 1

for i in range(1,n):
    for j in range(i):
        if i==j: continue
        if a[j] < a[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif a[j] > a[i]:
            dp[i][1] = max(dp[i][1] , dp[j][0] + 1, dp[j][1] + 1)



ans = 0
for i in range(n):
    ans = max(ans, dp[i][0], dp[i][1])

print(ans)