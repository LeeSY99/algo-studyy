n,k= map(int,input().split())
nums= list(map(int,input().split()))

import sys
cost=sys.maxsize
for i in range(min(nums),max(nums)+1-k):
    now_cost=0
    for j in range(n):
        if nums[j]<i:
            now_cost+=(i-nums[j])
        elif nums[j]>i+k:
            now_cost+=(nums[j]-(i+k))
    cost=min(cost,now_cost)

print(cost)