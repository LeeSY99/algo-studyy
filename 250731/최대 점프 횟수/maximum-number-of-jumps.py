n = int(input())
nums = list(map(int, input().split()))

dp = [-1] * n
dp[0] = 0

for i in range(1,n):
    for j in range(i):
        if dp[j] != -1 and j+nums[j] >= i:
            dp[i] = max(dp[i], dp[j]+1)
    # if dp[i] == 0:
    #     break

# print(*dp)
print(max(dp))