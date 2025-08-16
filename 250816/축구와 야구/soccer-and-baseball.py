n = int(input())
baseball = [0]
soccer = [0]

for i in range(n):
    s, b = map(int, input().split())
    soccer.append(s)
    baseball.append(b)

#dp[i][j][k]: i번째 사람 고려, j명 축구팀, k명 야구팀 -> 능력 합

dp = [[[float('-inf')] * (10) for _ in range(12)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(1,n+1):
    for j in range(12):
        for k in range(10):
            if i - (j+k) < 0:
                continue
            #아무데도 안감
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
            #축구부 간 경우
            if j>=1 and dp[i-1][j-1][k] != float('-inf'):
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + soccer[i])
            #야구부 간 경우
            if k>=1 and dp[i-1][j][k-1] != float('-inf'):
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + baseball[i])

print(dp[n][11][9])
