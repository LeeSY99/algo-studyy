n=int(input())

line=[0]*101

for _ in range(n):
    pos,alpha=input().split()
    pos=int(pos)
    line[pos]=alpha

max_len=0
for i in range(1,101):
    G=0
    H=0
    if line[i]==0:
        continue
    for j in range(i,101):
        if line[j]==0:
            continue
        if line[j]=='G':
            G+=1
        elif line[j]=='H':
            H+=1
        if (G==H and G!=0) or (G!=0 and H==0) or (H!=0 and G==0):
            max_len=max(max_len,j-i)
    
print(max_len)
