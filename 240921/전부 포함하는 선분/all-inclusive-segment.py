n=int(input())


x=[]
y=[]
for _ in range(n):
    ix,iy=map(int,input().split())
    x.append(ix)
    y.append(iy)

import sys
min_len=sys.maxsize
for i in range(n):
    min_x=sys.maxsize
    max_y=0
    for j in range(n):
        if i==j:
            continue
        min_x=min(min_x,x[j])
        max_y=max(max_y,y[j])
    min_len=min(min_len,max_y-min_x)
        
print(min_len)       

#완전 탐색 O(N^2)

#x가 가장 작은곳 이거나 y가 가장 큰 곳이 가능성 있음 그 2개를 비교하면 O(N)