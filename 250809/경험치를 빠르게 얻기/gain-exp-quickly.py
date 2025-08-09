''' n개 퀘스트 정보, 각 퀘스트로 부터 얻은 경험치 합이 m이상, 걸리는 시간 최소)

dp[i][j] - i번째 퀘스트까지 고려 j경험치 -> 최소 걸리는 시간

1) i번재 퀘스트 수행 dp[i][j] = min(dp[i][j], dp[i-1][j-arr[i]] + time[i])
2) i번쨰 퀘스트 수행x dp[i][j] = min(dp[i][j], dp[i-1][j])


'''

n,m = map(int, input().split())

arr = [(0,0)]
all_exp = 0
for _ in range(n):
    e, t = map(int, input().split())
    arr.append((e,t))
    all_exp += e

import sys
dp = [[sys.maxsize] * (all_exp+1) for _ in range(n+1)]
def initialize():
    for i in range(all_exp+1):
        dp[0][1] = 0
    for i in range(n+1):
        dp[i][0] = 0
initialize()
for i in range(1,n+1):
    for j in range(all_exp+1):
        exp, time = arr[i]
        if j-exp < 0 :
            continue
        
        #1)
        dp[i][j] = min(dp[i][j], dp[i-1][j-exp] + time)
        #2)
        dp[i][j] = min(dp[i][j], dp[i-1][j])

ans = sys.maxsize
for i in range(m, all_exp+1):
    ans = min(ans, dp[n][i])

ans = -1 if ans == sys.maxsize else ans
print(ans)

# for d in dp:
#     print(*d)