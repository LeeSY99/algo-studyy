''' 수정 샘터에서 생성, 땅에 떨어지면 소멸

소멸하기 전에 잡아야 함, k 번만 이동'''

n, k = map(int, input().split())
a = " " + input()
#초기 : 왼쪽
#dp[i][j][k] -> i수정 개수, j이동 횟수, k 현재 위치 



dp = [[[float('-inf') for _ in range(2)] for _ in range(k+2)] for _ in range(n+1)] 

dp[0][0][0] = 0
dp[0][1][1] = 0

for i in range(1,n+1):
    for j in range(k+1):
        if dp[i-1][j][0] != float('-inf'): #직전에 왼쪽에 있었음
            if a[i] == 'L': # 왼쪽에 떨어짐
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0] + 1)
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][0])
            else:   #오른쪽에 떨어짐
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][0] + 1)
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0])
        
        if dp[i-1][j][1] != float('-inf'): #직전에 오른쪽에 있었음
            if a[i] == 'L':
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][1] + 1)
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1])
            else:
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1] + 1)
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][1])

ans = 0
for j in range(k+1):
    ans = max(ans, dp[n][j][0], dp[n][j][1])

print(ans)