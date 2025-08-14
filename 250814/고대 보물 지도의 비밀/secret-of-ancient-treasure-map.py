n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

#dp[i][j] = i번째 숫자까지 고려, 연속된 음수j개 ->  연속합 최대

dp = [[float('-inf')] * (k+1) for _ in range(n+1)]

dp[0][0] = 0


for i in range(1,n+1):
        if arr[i] >= 0:
            for j in range(k+1):
                dp[i][j] = max( dp[i-1][j] + arr[i], arr[i])
        else:
            for j in range(1,k+1):
                dp[i][j] = max(dp[i-1][j-1] + arr[i], arr[i])

   
# for d in dp:
#     print(*d)
ans= float('-inf')
for i in range(1,n+1):
    for j in range(k+1):
        ans = max(ans, dp[i][j])
print(ans)