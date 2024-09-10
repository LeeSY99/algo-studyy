a,b,c= map(int,input().split())

count=0
while(1):
    if b-a==1 and c-b==1:
        break
    if b-a >= c-a:
        a=b+1
        a,b=b,a
        count+=1
    else:
        c=b-1
        b,c=c,b
        count+=1

print(count)