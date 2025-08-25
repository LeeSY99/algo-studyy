'''n층 신전 왼 가 오 방 

연속으로 같은 방향의 방을 들어갈 수 없음 

꼭데기층 1층 같은 방향 불가'''

n = int(input())

c = [[0,0,0]] + [list(map(int, input().split())) for _ in range(n)] 


dp = [[0]*3 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(3):
        for k in range(3): #이전 층
            if j == k: continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + c[i][j])
            if i == n:
                for l in range(3):
                    if j == k or l == j:
                        continue
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + c[i][j])


print(max(dp[n]))
                    
        

    