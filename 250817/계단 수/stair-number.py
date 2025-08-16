n = int(input())

#dp[i][j] : 길이가 i인수 중 마지막 자리수 숫자가 j 계단 수 개수

dp = [[0] * 10 for _ in range(n+1)]
for j in range(1,10):
    dp[1][j] = 1
for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] += dp[i-1][j+1]
        elif j==9:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]

# for d in dp:
#     print(*d)
print(sum(dp[n]) % (10**9+7))