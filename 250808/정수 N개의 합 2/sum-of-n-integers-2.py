n,k = map(int, input().split())

nums = [0] + list(map(int, input().split()))

prefix_sum = [0] * (n+1)
for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

import sys
ans = -sys.maxsize
for i in range(k, n+1):
    ans = max(ans, prefix_sum[i]-prefix_sum[i-k])
# print(prefix_sum)
print(ans)