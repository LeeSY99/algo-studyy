t,a,b=map(int,input().split())

line=[0]*1000
for _ in range(t):
    alphabet,number=input().split()
    line[int(number)]=alphabet

def in_range(n):
    return 0<=n and n<1000

special_count=0
for i in range(a,b+1):
    d1,d2=-1,-1
    d1_ok,d2_ok=False,False
    for j in range(1000):
        if in_range(i-j) and d1_ok==False:
            if line[i-j]=='S':
                d1=j
                d1_ok=True
        if in_range(i+j) and d1_ok==False:
            if line[i+j]=='S':
                d1=j
                d1_ok=True

        if in_range(i-j) and d2_ok==False:
            if line[i-j]=='N':
                d2=j
                d2_ok=True
        if in_range(i+j) and d2_ok==False:
            if line[i+j]=='N':
                d2=j
                d2_ok=True

        if d1_ok and d2_ok:
            if d1<=d2:
                special_count+=1
            break

print(special_count)