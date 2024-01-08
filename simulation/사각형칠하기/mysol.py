color=[[0]*2001 for _ in range(2001)]

x1,y1,x2,y2=map(int,input().split())
x1,y1,x2,y2=x1+1000,y1+1000,x2+1000,y2+1000
for i in range(x1,x2):
    for j in range(y1,y2):
        color[i][j]=1

x1,y1,x2,y2=map(int,input().split())
x1,y1,x2,y2=x1+1000,y1+1000,x2+1000,y2+1000
for i in range(x1,x2):
    for j in range(y1,y2):
        color[i][j]=0

width=0
for c in color:
    width+=sum(c)

if width==0:
    print(0)
else:
    x1,y1,x2,y2=2001,2001,0,0
    for i in range(2001):
        for j in range(2001):
            if color[i][j]==1:
                x1=min(x1,i)
                y1=min(y1,j)
                x2=max(x2,i)
                y2=max(y2,j)

    print((x2-x1+1)*(y2-y1+1))