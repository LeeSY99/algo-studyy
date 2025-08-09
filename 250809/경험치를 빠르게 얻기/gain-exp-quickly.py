''' n개 퀘스트 정보, 각 퀘스트로 부터 얻은 경험치 합이 m이상, 걸리는 시간 최소)

dp[i][j] - i번째 퀘스트까지 고려 시간의 합 -> 최대 경험치

1) i번재 퀘스트 수행 dp[i][j] = min(dp[i][j], dp[i-1][j-arr[i]] + time[i])
2) i번쨰 퀘스트 수행x dp[i][j] = min(dp[i][j], dp[i-1][j])


'''

n,m = map(int, input().split())


exp_list = [0]
time_list = [0]
for _ in range(n):
    e, t = map(int, input().split())
    exp_list.append(e)
    time_list.append(t)

all_time = sum(time_list)

import sys
dp = [[-sys.maxsize] * (all_time+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(all_time+1):
        if j-time_list[i]>=0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-time_list[i]] + exp_list[i])
        dp[i][j] = max(dp[i][j], dp[i-1][j])

ans = sys.maxsize
for i in range(all_time+1):
    if dp[n][i] >= m:
        ans = min(ans, i)

if ans == sys.maxsize:
    ans = -1
print(ans)

# for d in dp:
#     print(*d)