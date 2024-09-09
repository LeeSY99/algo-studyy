n,m,p=map(int,input().split())
info = [list(input().split()) for _  in range(m)]

people=[]
start='A'
for i in range(n):
    people.append(chr(ord(start)+i))

read=[]
not_read_msg=int(info[p-1][1])
for i in range(m):
    if i==p-1:
        if int(info[i][1])==0:
            exit()
    if int(info[i][1])==not_read_msg or i>=p-1:
        read.append(info[i][0])

ans=[]
for p in people:
    if p not in read:
        ans.append(p)
ans.sort()
for a in ans:
    print(a, end=' ')