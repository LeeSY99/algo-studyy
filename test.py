n=int(input())

points=[]
for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

import sys

minwidth=sys.maxsize
for i in range(n):
    x1,y1=sys.maxsize,sys.maxsize
    x2,y2=0,0
    for j in range(n):
        if i==j:
            continue
        x,y=points[j]
        x1=min(x1,x)
        y1=min(y1,y)
        x2=max(x2,x)
        y2=max(y2,y)
    width=(x2-x1)*(y2-y1)
    minwidth=min(minwidth,width)


print(minwidth)
        