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

dp = [[False] * (m+1) for _ in range(n+1)]

dp[0][0] = True

for i in range(1,n+1):
    for j in range(m+1):
        if j >= arr[i] and dp[i-1][j-arr[i]]:
            dp[i][j] = True

        if dp[i-1][j]:
            dp[i][j] = True
        
if m%2 == 0 and dp[n][m//2]:
    print('Yes')
else:
    print('No')


