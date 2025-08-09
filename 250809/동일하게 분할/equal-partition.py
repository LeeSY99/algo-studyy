# n = int(input())
# arr = [0] + list(map(int, input().split()))

''' dp[i][j] = i번째 수까지 고려 j:i그룹의 합 -> a-b그룹 차이 최소
1) i번쨰 수를 a에 넣음
dp[i][j] = dp[i-1][j-arr[i]] + arr[i] 
2) i번째 수를 b에 넣음
dp[i][j] = dp[i-1][j-arr[i]] - arr[i]


---------------
dp[i]: i번 쨰 원소 고려 a그룹의 합

'''
import sys

n = int(input())
arr = [0] + list(map(int, input().split()))

m = sum(arr)
INF = sys.maxsize
dp_prev = [INF] * (m+1)
dp_prev[0] = 0

for i in range(1, n+1):
    dp_curr = [INF] * (m+1)
    for j in range(m+1):
        if dp_prev[j] != INF:
            if j + arr[i] <= m:
                dp_curr[j + arr[i]] = min(dp_curr[j + arr[i]], dp_prev[j] + arr[i])
            dp_curr[j] = min(dp_curr[j], dp_prev[j] - arr[i])
    dp_prev = dp_curr

print("Yes" if 0 in dp_prev else "No")
