n=int(input())
dx,dy=[1,0,-1,0],[0,-1,0,1]

nx,ny=0,0
for _ in range(n):
    command,k=input().split()
    k=int(k)

    if command=="E":
        nx+=dx[0]*k
        ny+=dy[0]*k
    elif command=="S":
        nx+=dx[1]*k
        ny+=dy[1]*k
    elif command=="W":
        nx+=dx[2]*k
        ny+=dy[2]*k
    elif command=="N":
        nx+=dx[3]*k
        ny+=dy[3]*k
print(nx,ny)