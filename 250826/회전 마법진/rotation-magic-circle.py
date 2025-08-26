n = int(input())

now = [0] + list(map(int, input()))
nxt = [0] + list(map(int, input()))

#dp[i][j] : i번째 마법진 맞춰짐, j번 역회전 -> 최소 회전수
dp = [[float('inf') for _ in range(10) ] for _ in range(n+1)]
dp[0][0] = 0


for i in range(n):
    for j in range(10):
        if dp[i][j] == float('inf'): continue
        cur = (now[i+1] + j) % 10
        target = nxt[i+1]
        
        #반시계
        cost = (target - cur + 10) % 10
        nj = (j+cost) % 10
        dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + cost)

        #시계
        cost = (cur - target + 10) % 10
        nj = j
        dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + cost)

ans = min(dp[n])
# for d in dp:
#     print(*d)
print(ans)
        