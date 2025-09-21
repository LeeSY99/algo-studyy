n = int(input())
nums = list(map(int, input().split()))

import sys
ans = -sys.maxsize
now_sum = 0
for i in range(n):
    now_sum += nums[i]
    ans = max(ans, now_sum)
    if now_sum < 0:
        now_sum = 0

print(ans)

