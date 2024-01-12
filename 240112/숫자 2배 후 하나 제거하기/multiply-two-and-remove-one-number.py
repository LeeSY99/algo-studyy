n=int(input())

nums=list(map(int,input().split()))

import sys
min_sum=sys.maxsize
for i in range(n):
    nums[i]*=2

    for j in range(n):
        remain=[]
        for k,elem in enumerate(nums):
            if j!=k:
                remain.append(elem)
    
        diff_sum=0
        for k in range(n-2):
            diff_sum += abs(remain[k]-remain[k+1])
        min_sum=min(min_sum,diff_sum)
    nums[i] //=2

print(min_sum)