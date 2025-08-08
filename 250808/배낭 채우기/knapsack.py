n,m = map(int, input().split())

weight = [0]
value = [0]

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

#dp[i][j\]: i보석 고려. 고른 보석의 무게 합j -> 얻는 최대가치
dp = [[0] * (m+1) for _ in range(n+1)]

#1) i번보석을 배낭에 넣음
#2) i번보석을 선택하지 않음
for i in range(1,n+1):
    for j in range(m+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j] )
        else:
            dp[i][j] = dp[i-1][j]
        

ans = 0
for j in range(m+1):
    ans = max(ans, dp[n][j])

print(ans)




