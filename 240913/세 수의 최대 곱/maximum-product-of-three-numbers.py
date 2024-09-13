n=int(input())
nums=list(map(int,input().split()))
nums.sort()
# print(nums)

plus_count=0
zero_count=0
minus_count=0

for num in nums:
    if num<0:
        minus_count+=1
    elif num ==0:
        zero_count+=1
    else:
        plus_count+=1

import sys
ans=-sys.maxsize
#양수 없음
if plus_count==0 and zero_count==0:
    ans=nums[n-1]*nums[n-2]*nums[n-3]
elif plus_count==0 and zero_count!=0:
    ans=0

#양수 3개 이상
if plus_count>=3:
    ans=max(ans,nums[n-1]*nums[n-2]*nums[n-3])
    ans=max(ans,nums[0]*nums[1]*nums[n-1])
elif 1<=plus_count<=2:
    ans=nums[0]*nums[i]*nums[n-1]

print(ans)