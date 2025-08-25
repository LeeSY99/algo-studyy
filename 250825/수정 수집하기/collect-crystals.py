''' 수정 샘터에서 생성, 땅에 떨어지면 소멸

소멸하기 전에 잡아야 함, k 번만 이동'''

n, k = map(int, input().split())
a = " " + input()
#초기 : 왼쪽
#dp[i][j][k] -> i수정 개수, j이동 횟수, k 현재 위치 



dp = [[[float('-inf') for _ in range(2)] for _ in range(k+2)] for _ in range(n+1)] 

dp[0][0][0] = 0
dp[0][1][1] = 0

for i in range(n):
    for j in range(k+1):
        if dp[i][j][0] != float('-inf'): #현재위치 왼쪽
            if a[i+1] == 'L':
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0] + 1)
                dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][0])
            else:
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0])
                dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][0] + 1)
        
        if dp[i][j][1] != float('-inf'): #현재위치 오른쪽
            if a[i+1] == 'L':
                dp[i+1][j+1][0] = max(dp[i+1][j+1][0], dp[i][j][1] + 1)
                dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1])
            else:
                dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1] + 1)
                dp[i+1][j+1][0] = max(dp[i+1][j+1][0], dp[i][j][1])
ans = 0
for j in range(k+1):
    ans = max(ans, dp[n][j][0], dp[n][j][1])

print(ans)