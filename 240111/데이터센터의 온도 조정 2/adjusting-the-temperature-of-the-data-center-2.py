n,c,g,h=map(int,input().split())

def tem(t,a,b):
    if t<a:
        return c
    elif t<=b:
        return g
    else:
        return h
import sys
tem_range=[]
min_temp=sys.maxsize
max_temp=0
for _ in range(n):
    ta,tb=map(int,input().split())
    tem_range.append([ta,tb])
    min_temp=min(min_temp,ta)
    max_temp=max(max_temp,tb)

best_work=0
for t in range(min_temp-1,max_temp+2):
    now_work=0
    for ta,tb in tem_range:
        now_work+=tem(t,ta,tb)
    best_work=max(best_work,now_work)

print(best_work)