n=int(input())

instr=input()
arr=[]
for s in instr:
    arr.append(int(s))

import sys
max_distance=0
for i in range(n):
    if arr[i]==1:
        continue
    else:
        arr[i]=1
        min_distance=sys.maxsize
        for j in range(n):
            for k in range(j+1,n):
                if arr[j]==1 and arr[k]==1:
                    distance=k-j
                    min_distance=min(min_distance,distance)
        arr[i]=0
        max_distance=max(max_distance,min_distance)

print(max_distance)