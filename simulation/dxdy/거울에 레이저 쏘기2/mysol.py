n=int(input())

up=0
down=1
left=2
right=3

mirror=[[0]*(n+2)]
for i in range(n):
    a=[0]
    inl=list(input())
    for i in inl:
        a.append(i)
    a.append(0)
    mirror.append(a)

mirror.append([0]*(n+2))

start=int(input())

def in_range(r,c):
    return 1<=r and r<=n and 1<=c and c<=n

lrr,lrc=[0,1,0,-1],[1,0,-1,0]
rlr,rlc=[0,-1,0,1],[-1,0,1,0]

if (start-1)//n==0:
    sr=0
    sc=start
    direction=down
elif (start-1)//n==1:
    sr=start-n
    sc=n+1
    direction=left
elif (start-1)//n==2:
    sr=n+1
    sc=(n*3+1)-start
    direction=up
else:
    sr=(n*4+1)-start
    sc=0
    direction=right

if direction ==down:
    nr,nc=sr+1,sc
elif direction == left:
    nr,nc=sr,sc-1
elif direction == up:
    nr,nc=sr-1,sc
else:
    nr,nc=sr,sc+1

count=0
while in_range(nr,nc):
    if mirror[nr][nc]=='\\':
        if direction==down:
            nr,nc=nr+lrr[0],nc+lrc[0]
            direction=right
        elif direction==right:
            nr,nc=nr+lrr[1],nc+lrc[1]
            direction=down
        elif direction==up:
            nr,nc=nr+lrr[2],nc+lrc[2]
            direction=left
        elif direction==left:
            nr,nc=nr+lrr[3],nc+lrc[3]
            direction=up

    else:
        if direction==down:
            nr,nc=nr+rlr[0],nc+rlc[0] 
            direction=left
        elif direction==right:
            nr,nc=nr+rlr[1],nc+rlc[1] 
            direction=up
        elif direction==up:
            nr,nc=nr+rlr[2],nc+rlc[2] 
            direction=right
        elif direction==left:
            nr,nc=nr+rlr[3],nc+rlc[3] 
            direction=down
    count+=1
print(count)
