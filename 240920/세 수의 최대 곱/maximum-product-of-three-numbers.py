n=int(input())

nums=list(map(int,input().split()))

nums.sort()

zero_start=-1
for i in range(n):
    if nums[i]==0:
        zero_start=i
        break

plus_start=-1
for i in range(n):
    if nums[i]>0:
        plus_start=i
        break

import sys
ans=-sys.maxsize

#양양양
if zero_start>=2:
    ans=max(ans,nums[-1]*nums[-2]*nums[-3])

#음음양
ans=max(ans,nums[0]*nums[1]*nums[-1])

ans=max(ans,nums[0]*nums[1]*nums[2])

print(ans)