n,m = map(int, input().split())

coins = [0]
coins += list(map(int, input().split()))
import sys
dp = [sys.maxsize] * (m+1)
dp[0] = 0

for i in range(1,m+1):
    for j in range(n+1):
        if i-coins[j] <0:
            continue
        dp[i] = min(dp[i], dp[i-coins[j]] + 1)

# print(*dp)
ans = -1 if dp[m] == sys.maxsize else dp[m]
print(ans)
