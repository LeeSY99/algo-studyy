n = int(input())

arr = [(0,0)] + [tuple(map(int, input().split())) for _ in range(2*n)]
# print(arr)

#dp[i][j] : i번 실행 빨간색카드 j번 선택 -> 뽑힌 숫자의 합
dp = [[float('-inf')]*(n+1) for _ in range(2*n + 1)]

dp[0][0] = 0

for i in range(1,2*n+1):
    a, b = arr[i]
    dp[i][0] = dp[i-1][0] + b
    up = min(i,n)
    for j in range(1, up+1):
        dp[i][j] = max(dp[i-1][j-1] + a, dp[i-1][j] + b)
        
print(dp[2*n][n])

# for d in dp:
#     print(*d)
