n = int(input())

arr = [0] + list(map(int, input().split()))

#dp[i][j] = i번째 계단까지 고려 개단 오른 횟수 -> 최대 동전 수
dp = [[0] * 4 for _ in range(n+1)]

dp[0][0] = 0

for i in range(1,n+1):
    for j in range(1,4):
        if i-j<0: continue
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i], dp[i-2][j] + arr[i])

# for d in dp:
#     print(*d)
print(dp[n][3])


