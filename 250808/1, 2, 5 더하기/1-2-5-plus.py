n = int(input())

nums = [1,2,5]

#dp[i] = 합이 i인 식의 가지수
dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n+1):
    for num in nums:
        if i-num >=0:
            dp[i] = (dp[i] + dp[i-num])%10007

print(dp[n])