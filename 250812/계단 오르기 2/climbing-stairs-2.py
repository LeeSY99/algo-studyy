n = int(input())

arr = [0] + list(map(int, input().split()))

#dp[i][j] = i번째 계단까지 고려 1번오른 칸수 j-> 최대 동전 수
dp = [[0] * (4) for _ in range(n+1)]

dp[0][0] = 0
dp[1][1] = arr[1]

if n > 1:
    dp[2][0] = arr[2]
    dp[2][2] = arr[1] + arr[2]

for i in range(3,n+1):
    for j in range(4):
        if dp[i-2][j] != 0 :
            dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])
        if j and dp[i-1][j-1] != 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])
        
        

# for d in dp:
#     print(*d)
ans = max(dp[n])
print(ans)


