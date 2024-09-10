n=int(input())

in_data=input()
desk=[]

max_interval=0
for i in range(n):
    for j in range(i+1,n):
        if in_data[i]=='1' and in_data[j]=='1':
            if max_interval < j-i:
                start=i
                end=j
                max_interval=j-i
            break

desk=list(in_data)
desk[(end-start)//2] = '1'

import sys
min_interval=sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        if desk[i]=='1' and desk[j]=='1':
            min_interval=min(min_interval,j-i)
            break

print(min_interval)