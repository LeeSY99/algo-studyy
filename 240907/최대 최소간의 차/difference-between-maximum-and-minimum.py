n,k= map(int,input().split())
nums= list(map(int,input().split()))

import sys
cost=sys.maxsize
for i in range(min(nums),max(nums)+1-k):#nums의 최소와 최대에서 k작은 구간만 탐색 ->
    now_cost=0
    for j in range(n):
        if nums[j]<i:                   #nums를 순회하면서 예상 최소보다 작으면 비용추가
            now_cost+=(i-nums[j])
        elif nums[j]>i+k:               #예상 최대보다 크면 비용추가
            now_cost+=(nums[j]-(i+k))
    cost=min(cost,now_cost)

print(cost)