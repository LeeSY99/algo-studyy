x11,y11,x12,y12=map(int,input().split())
x21,y21,x22,y22=map(int,input().split())

width=max(x12,x22)-min(x11,x21)
height=max(y12,y22)-min(y11,y21)

print(max(width,height)**2)