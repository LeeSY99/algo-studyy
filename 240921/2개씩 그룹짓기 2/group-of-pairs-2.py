n=int(input())

nums=list(map(int,input().split()))

nums.sort(reverse=True)

import sys
ans=sys.maxsize

for i in range(n):
    d=nums[i]-nums[i+n]
    ans=min(ans,d)

print(ans)