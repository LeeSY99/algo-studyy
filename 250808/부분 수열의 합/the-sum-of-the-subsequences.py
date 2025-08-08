n, m = map(int, input().split())
arr = list(map(int, input().split()))

#dp[i] = 합이 i일떄 부분수열이 있는지
dp = [False] * (m+1)
dp[0] = True

for i in range(n):
    for j in range(m,-1,-1):
        if j-arr[i] >= 0:
            if dp[j-arr[i]]:
                dp[j] = True


print('Yes' if dp[m] else 'No')
