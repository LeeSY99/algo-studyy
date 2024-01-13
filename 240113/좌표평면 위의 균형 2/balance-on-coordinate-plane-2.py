n=int(input())

points=[list(map(int,input().split())) for _ in range(n)]

import sys
ans=sys.maxsize
for i in range(2,101,2): #i->x축
    for j in range(2,101,2): #j->y축
        one,two,three,four=0,0,0,0
        for x,y in points:
            if x>j and y>i:
                one+=1
            elif x<j and y>i:
                two+=1
            elif x<j and y<i:
                three+=1
            else:
                four+=1
        max_points=max(one,two,three,four)
        ans=min(ans,max_points)

print(ans)