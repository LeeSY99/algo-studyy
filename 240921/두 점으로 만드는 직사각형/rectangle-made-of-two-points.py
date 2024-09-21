x1,y1,x2,y2=map(int,input().split())
a1,b1,a2,b2=map(int,input().split())

6688
1849
1689

leftx=min(x1,a1)
lefty=min(y1,b1)
rightx=max(x2,a2)
righty=max(y2,b2)

print(abs(rightx-leftx)*abs(righty-lefty))