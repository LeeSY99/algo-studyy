n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

for i in range(1,n):
    for j in range(i):
        if j+nums[j] >= i:
            dp[i] = max(dp[i], dp[j]+1)
    if dp[i] == 0:
        break

# print(dp)
ans = 1
print(max(ans,dp[n-1]))