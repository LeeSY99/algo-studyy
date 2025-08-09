n = int(input())
arr = [0] + list(map(int, input().split()))

''' dp[i][j] = i번째 수까지 고려 j:i그룹의 합 -> a-b그룹 차이 최소
1) i번쨰 수를 a에 넣음
dp[i][j] = dp[i-1][j-arr[i]] + arr[i] 
2) i번째 수를 b에 넣음
dp[i][j] = dp[i-1][j-arr[i]] - arr[i]


'''
import sys

m = sum(arr)
dp = [[sys.maxsize] * (m+1) for _ in range(m)]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(1, m+1):
        if j - arr[i] >= 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j-arr[i]] + arr[i])
        dp[i][j] = min(dp[i][j], dp[i-1][j] - arr[i])

# print(dp[n])
ans = 'No'
for d in dp[n]:
    if d == 0:
        ans = 'Yes'

print(ans)
