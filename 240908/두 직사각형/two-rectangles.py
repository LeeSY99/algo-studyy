x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())

overlap=1
if x2<a1:
    overlap=0
elif a2<x1:
    overlap=0
elif y2<b1:
    overlap=0
elif b2<y1:
    overlap=0

if overlap:
    print('overlapping')
else:
    print('nonoverlapping')