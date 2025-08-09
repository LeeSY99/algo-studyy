#dp[i][j]  i번째 수까지 고려했을떄 a의 합-b의 합이 j일때 ->a의 최대합

#1)a에 넣을때 dp[i][j] = max(dp[i][j], dp[i-1][j-arr[i]] + arr)
#2)b에 넣을때 dp[i][j] = max(dp[i][j], dp[i-1][j+arr[i]])
#3)c에 버림 dp[i][j] = max(dp[i][j], dp[i-1][j])
# ->dp[n][0] 을 조회하면 n번쨰 수까지 고려하고 차이가 0이라 합이 같음 그때의 a의 최대합
import sys
n = int(input())
arr = [0] + list(map(int, input().split()))

offset = 1000 * 100

m = sum(arr)
dp = [[0]*(m+1+offset) for _ in range(n+1)]

def initialize():
    for i in range(n+1):
        for j in range(-m, m+1):
            dp[i][j+offset] = -sys.maxsize
    dp[0][0+offset] = 0

def update(i,j,prev_i, prev_j, value):
    if prev_j < -m or prev_j > m or dp[prev_i][prev_j+offset] == -sys.maxsize:
        return
    
    dp[i][j+offset] = max(dp[i][j+offset], dp[prev_i][prev_j+offset] + value)

initialize()
for i in range(1,n+1):
    for j in range(-m, m+1):
        #1)
        update(i,j, i-1, j-arr[i], arr[i])
        #2)
        update(i,j, i-1, j+arr[i], 0)
        #3)
        update(i,j, i-1, j, 0)

print(dp[n][0+offset])    