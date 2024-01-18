n,k=map(int,input().split())

arr=list(map(int,input().split()))

def available(max_val):
    available_num=[]
    for i, num in enumerate(arr):
        if num<=max_val:
            available_num.append(i)

    for i in range(1,len(available_num)):
        if available_num[i]-available_num[i-1]>k:
            return False
    return True

import sys
ans=sys.maxsize
for n in range(max(arr[1],arr[-1]),101):
    if available(n):
        ans=min(ans,n)
print(ans)