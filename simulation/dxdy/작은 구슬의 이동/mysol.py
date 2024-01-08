n,t=map(int,input().split())
r,c,d=input().split()
r=int(r)
c=int(c)
dr=[0,1,0,-1]
dc=[1,0,-1,0]
dir=0

def in_range(nr,nc):
    return 0<nr<=n and 0<nc<=n

if d=='R':
    dir=0
elif d=='D':
    dir=1
elif d=='L':
    dir=2
elif d=='U':
    dir=3

for _ in range(t):
    nr = r+ dr[dir]
    nc = c+ dc[dir]
    if in_range(nr,nc):
        r,c=nr,nc
    else:
        dir=(dir+2)%4

print(r,c)
#O(t)