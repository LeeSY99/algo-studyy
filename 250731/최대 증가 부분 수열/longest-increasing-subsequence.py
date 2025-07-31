n = int(input())
# nums = [0]
nums = list(map(int, input().split()))

dp = [1] * (n)
dp[0] = 1

for i in range(n):
    for j in range(i-1,-1,-1):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))