'''n층 신전 왼 가 오 방 

연속으로 같은 방향의 방을 들어갈 수 없음 

꼭데기층 1층 같은 방향 불가'''

n = int(input())

c = [[0,0,0]] + [list(map(int, input().split())) for _ in range(n)] 


dp = [[[0]*3 for _ in range(3)] for _ in range(n+1)]
for j in range(3):
    dp[1][j][j] = c[1][j]

#dp[i][j][k]: i층  j:1층에서 선택한 방, k: i번째 층에서 선택한 방
for i in range(2,n+1):
    for j in range(3):
        for k in range(3): 
            for l in range(3): #직전 층 
                if k == l: continue
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l] + c[i][k])
            

ans = 0
for j in range(3):
    for k in range(3):
        if j == k: continue
        ans = max(ans, dp[n][j][k])

# for d in dp:
#     print(*d)
print(ans)
                    
        

    