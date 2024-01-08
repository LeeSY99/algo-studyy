commands=input()

dx=[0,1,0,-1]
dy=[1,0,-1,0]
dir=0
x,y=0,0
for command in commands:
    if command=='L':
        dir=(dir-1)%4
    elif command=='R':
        dir=(dir+1)%4
    elif command=='F':
        x+=dx[dir]
        y+=dy[dir]

print(x,y)

#시간복잡도 O(n)