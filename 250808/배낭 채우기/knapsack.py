n,m = map(int, input().split())

weight = [0]
value = [0]

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

#n번쨰 보석 고려시 무게, 최대value
dp = [[0,0] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(i):
        if dp[j][0] + weight[i] <= m:
            if dp[j][1] + value[i] > dp[i][1]:
                dp[i][0] = dp[j][0] + weight[i]
                dp[i][1] = dp[j][1] + value[i]

ans = 0
for d in dp:
    ans = max(ans, d[1])

print(ans)




