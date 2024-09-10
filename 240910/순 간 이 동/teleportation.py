A,B,x,y = map(int,input().split())

c1=B-A
if x>y:
    c2=abs(y-A)+abs(B-x)
    print(min(c1,c2))
else:
    c3=abs(x-A)+abs(B-y)
    print(min(c1,c3))