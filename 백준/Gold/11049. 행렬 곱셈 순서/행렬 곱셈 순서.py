n = int(input())
arr= [(0,0)]
for _ in range(n):
    r,c = map(int, input().split())
    arr.append((r,c))

#dp[i][j] i번 행령~j번행렬 곱하는 최소
dp = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i] = 0
# for d in dp:
#     print(*d)
# print('--')
def cost(i,k,j):
    return arr[i][0] * arr[k][1] * arr[j][1]
for length in range(2,n+1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost(i,k,j))

# for d in dp:
#     print(*d)
print(dp[1][n])