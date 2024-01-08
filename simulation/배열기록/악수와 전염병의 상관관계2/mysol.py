N,K,P,T=map(int,input().split())

infected=[0]*(N+1)
shaked=[0]*(N+1)
infected[P]=1

time=[]
a=[]
b=[]
for i in range(T):
    t,x,y=map(int,input().split())
    time.append(t)
    a.append(x)
    b.append(y)

for i in range(1,251):
    if i in time:
        index=time.index(i)
        if infected[a[index]] or infected[b[index]]:
            if infected[a[index]]:
                shaked[a[index]]+=1
            if infected[b[index]]:
                shaked[b[index]]+=1
            if shaked[a[index]]<=K and shaked[b[index]]<=K:
                infected[a[index]]=1
                infected[b[index]]=1
            
            
for i in range(1,N+1):
    print(infected[i],end='')