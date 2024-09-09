n,m,p=map(int,input().split())
info = [list(input().split()) for _  in range(m)]

people=[]
start='A'
for i in range(n):
    people.append(chr(ord(start)+i))

read=[]
for i in range(p-1,m):
    if int(info[i][1])==0:
        exit()
    if i>0 and info[i-1][1]==info[i][1]:
        read.append(info[i-1][0])
    read.append(info[i][0])

ans=[]
for p in people:
    if p not in read:
        ans.append(p)
ans.sort()
for a in ans:
    print(a, end=' ')