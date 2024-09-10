a,b,c=map(int,input().split())



if c-b==1 and b-a==1:
    count=0
elif c-b==2 or b-a ==2:
    count=1
else:
    count=2

print(count)