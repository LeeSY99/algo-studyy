n=int(input())
nums=list(map(int,input().split()))

import sys
min_idx=0
min_num=min(nums)
min_interval=sys.maxsize

for i in range(n):
    if nums[i] == min_num:
        continue
    if nums[i]-min_num<min_interval:
        min_interval=nums[i]-min_num
        min_count=1
        min_idx=i
    elif nums[i]-min_num<min_interval:
        min_count+=1

if min_count==1:
    print(min_idx+1)
else:
    print(-1)