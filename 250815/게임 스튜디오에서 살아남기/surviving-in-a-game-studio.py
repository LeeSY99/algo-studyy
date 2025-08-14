n = int(input())

#dp[i][j][k] i번째 평가, 연속j번 b, k번 t받음 -> 가지수

dp = [[[0] * 3 for _ in range(3)] for _ in range(n+1)]

dp[0][0][0] = 1
for i in range(1, n+1):
    #t가 들어온 경우
    for k in range(3):
        dp[i][0][k] += dp[i-1][0][k] + dp[i-1][1][k] + dp[i-1][2][k]
    #b가 들어온 경우
    for k in range(3):
        dp[i][1][k] += dp[i-1][0][k]
        dp[i][2][k] += dp[i-1][1][k] 
    #t가 들어온 경우
    for k in range(1,3):
        dp[i][0][k] += dp[i-1][0][k-1] + dp[i-1][1][k-1] + dp[i-1][2][k-1]

ans = 0
for j in range(3):
    for k in range(3):
        ans += dp[n][j][k]

print(ans % (10**9+7))
            

# for d in dp:
#     print(*d)