n,m = map(int, input().split())
a = list(map(int, input().split()))
import sys
#dp[i] = 지금까지의 합이 i일때 최소 수열 길이
dp = [sys.maxsize] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(m,-1,-1):
        if j - a[i] >=0:
            dp[j] = min(dp[j], dp[j-a[i]] + 1)

min_len = dp[m]

if min_len == sys.maxsize:
    min_len = -1

print(min_len)