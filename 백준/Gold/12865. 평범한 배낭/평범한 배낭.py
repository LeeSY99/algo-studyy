n, k = map(int, input().split())

thing = [(0,0)]
for _ in range(n):
    w, v = map(int, input().split())
    thing.append((w,v))


#dp[i][j]: i번 물건까지 고려, 가방무게 j -> 최고의 가치

dp = [[0] * (k+1)  for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        now_w, now_v = thing[i]
        #1) 현재 물건 선택 or 선택x
        if j - now_w >= 0:
            dp[i][j] = max(dp[i-1][j-now_w] + now_v, dp[i-1][j])
        #2) 선택못함
        else:
            dp[i][j] = dp[i-1][j]

ans = 0
for i in range(k+1):
    ans = max(ans, dp[n][i])

print(ans)
