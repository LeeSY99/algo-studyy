n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    a = 0
    for j in range(i):
        a += dp[j] * dp[i-j-1]
    dp[i] = a

print(dp[n])