n=int(input())
lines=[]


for _ in range(n):
    a,b=map(int,input().split())
    lines.append((a,b))
    
count=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x=[0]*101
            for l in range(n):
                if i==l or j==l or k==l:
                    continue
                for m in range(lines[l][0],lines[l][1]+1):
                    x[m]+=1
            ok=True
            for o in range(101):
                if x[o]>1:
                    ok=False
                    break
            if ok:
                count+=1
print(count)