n=int(input())

in_data=list(input())
import sys
max_interval=0

for i in range(n):
    desk=in_data[:]
    if desk[i]=='1':
        continue
    desk[i]='1'

    min_interval=sys.maxsize
    for j in range(n):
        for k in range(j+1,n):
            if desk[j]=='1' and desk[k]=='1':
                min_interval=min(min_interval,k-j)
                break
    max_interval=max(max_interval,min_interval)

print(max_interval)