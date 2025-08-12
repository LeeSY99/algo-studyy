n = int(input())
nums = list(map(int, input().split()))
import sys

dp = [-sys.maxsize] * (n+1)
dp[0] = nums[0]

for i in range(1,n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

ans = -sys.maxsize
for i in range(n):
    ans = max(ans,dp[i])

print(ans)