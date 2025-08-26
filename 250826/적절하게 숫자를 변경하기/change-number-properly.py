''' 비슷한 수열: 인접한 두 숫자가 다른 횟수가 M번 이하 
유사도: 같은 위치에 같은 원소가 나온 횟수'''

n,m = map(int, input().split())
num = [0] + list(map(int, input().split()))

#dp[i][j] i번째 숫자까지 확인, j: 변경한 횟수, k가 마지막 사용 수 -> 유사도

dp = [[[float('-inf')] * (n) for _ in range(5)] for _ in range(n+1)]
for k in range(1,5):
    if k == num[1]:
        dp[1][0][k] = 1
    else:
        dp[1][0][k] = 0

for i in range(2,n+1):
    for j in range(m+1):
        for k in range(1,5): 
            for l in range(1,5): #직전에 사용한 숫자 l
                if l==k:
                    if k == num[i]:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l] + 1)
                    else:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l])
                if l!=k and j>0:
                    if k == num[i]:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l] + 1)
                    else:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l])

ans = 0
for j in range(m+1):
    for k in range(1,5):
        ans = max(ans, dp[n][j][k])

print(ans)


            

