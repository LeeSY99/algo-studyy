n,m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
p_s = [0] * (n+1)
for i in range(1,n+1):
    p_s[i] = p_s[i-1]+arr[i]

#dp[i][j] = i번쨰 숫자까지 고려 j개의 구간, 최대값

dp = [[float('-inf')] * (m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0

for j in range(1, m+1):
    best = float('-inf')
    for i in range(1,n+1):
        if i>=2:
            prev = dp[i-2][j-1]
        else:
            prev = 0 if j==1 else float('-inf')
        best = max(best,prev-p_s[i-1])

        dp[i][j] = max(dp[i-1][j], p_s[i] + best) 
        
print(dp[n][m])
# for d in dp:
#     print(*d)
        
