t,a,b=map(int,input().split())

line=[0]*1000
points=[tuple(input().split()) for _ in range(t)]

import sys
special_count=0
for i in range(a,b+1):
    d1,d2=sys.maxsize,sys.maxsize

    for a,x in points:
        x=int(x)

        if a=='S':
            d1=min(d1,abs(x-i))
        if a=="N":
            d2=min(d2,abs(x-i))
    if d1<=d2:
        special_count+=1
    

print(special_count)