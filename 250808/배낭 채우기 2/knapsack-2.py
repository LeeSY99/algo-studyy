n, m = map(int, input().split())
weight = [0]
value = [0]

for _ in range(n):
    w,v = map(int, input().split())
    weight.append(w)
    value.append(v)


#dp[i][j] i번 보석 고려 무게j -> 최대가치
#1) i번 선택
#2) i번 선택 x

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        #1)
        now_weight = j
        count = 0
        if j - weight[i] > 0:
            while now_weight >= 0:
                dp[i][j] = max(dp[i][j], dp[i-count][now_weight] + value[i]*count, dp[i-1][j])
                now_weight -= weight[i]
                count+=1
        else:
            dp[i][j] = max(dp[i][j] , dp[i-1][j])


ans = 0
for j in range(m+1):
    ans = max(ans, dp[n][j])

print(ans)
