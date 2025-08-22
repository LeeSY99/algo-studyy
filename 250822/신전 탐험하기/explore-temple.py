n = int(input())

#dp[i][j] i번째 층 0,1,2 완 가 오 로 올라온 경우
castle = [[0,0,0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(3):
        for k in range(3):
            if j == k: continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + castle[i][j])


print(max(dp[n]))
