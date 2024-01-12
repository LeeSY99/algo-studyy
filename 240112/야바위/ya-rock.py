n=int(input())

change=[list(map(int,input().split())) for _ in range(n)]

max_count=0
for i in range(3):
    rock=[0]*3
    rock[i]=1
    count=0
    for j in range(n):
        a,b,c=change[j][0]-1,change[j][1]-1,change[j][2]-1
        rock[a],rock[b]=rock[b],rock[a]
        if rock[c]==1:
            count+=1
    max_count=max(max_count,count)

print(max_count)