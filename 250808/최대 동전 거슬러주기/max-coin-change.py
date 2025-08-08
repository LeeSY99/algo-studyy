n, m = map(int, input().split())
coins = list(map(int, input().split()))

#dp[i] = i원을 거슬러줄 최대 동전의 개수
import sys
dp = [-sys.maxsize] * (m+1)
dp[0] = 0

for i in range(1,m+1):
    for coin in coins:
        if i-coin >= 0 and dp[i-coin] != -sys.maxsize:
            dp[i] = max(dp[i], dp[i-coin] + 1)

ans = dp[m]
if ans == -sys.maxsize:
    ans = -1
print(ans)