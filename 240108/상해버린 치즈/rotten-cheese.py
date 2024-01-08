n,m,d,s=map(int, input().split())

rotten=[0]*(m+1)
medicine=[0]*n

first=[]
second=[]
for _ in range(d):
    p,m,t=map(int,input().split())
    first.append((p,m,t))
    

for _ in range(s):
    p,t=map(int,input().split())
    second.append((p,t))


for s in second:
    for f in first:
        if f[0]==s[0] and f[2]<s[1]:
            rotten[f[1]] +=1


for i in range(1,len(rotten)):
    if rotten[i]==max(rotten):
        for f in first:
            if i==f[1]:
                medicine[f[0]-1]=1

print(sum(medicine))