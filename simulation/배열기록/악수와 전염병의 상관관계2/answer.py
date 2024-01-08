class Shake:
    def __init__(self,time,p1,p2):
        self.time=time
        self.p1=p1
        self.p2=p2

shakes=[]
n,k,p,t=map(int,input().split())
for _ in range(t):
    time,p1,p2=map(int,input().split())
    shakes.append(Shake(time,p1,p2))

shaked_num=[0]*(n+1)
infected=[0]*(n+1)

infected[p]=1

shakes.sort(key= lambda x:x.time)

for shake in shakes:
    target1=shake.p1
    target2=shake.p2

    if infected[target1]:
        shaked_num[target1]+=1
    if infected[target2]:
        shaked_num[target2]+=1

    if infected[target1] or infected[target2]:
        if shaked_num[target1]<=k and shaked_num[target2]<=k:
            infected[target1]=1
            infected[target2]=1

for i in range(1,n+1):
    print(infected[i],end='')