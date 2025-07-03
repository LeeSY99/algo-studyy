n = int(input())

dx, dy = [1,-1,0,0],[0,0,-1,1]

x,y = 0,0
for _ in range(n):
    direction, t = input().split()
    if direction == 'E':
        x= x+ (dx[0]*int(t))
        y= y+ (dy[0]*int(t))
    elif direction == 'W':
        x= x+ (dx[1]*int(t))
        y= y+ (dy[1]*int(t))
    elif direction == 'S':
        x= x+ (dx[2]*int(t))
        y= y+ (dy[2]*int(t))
    elif direction == 'N':
        x= x+ (dx[3]*int(t))
        y= y+ (dy[3]*int(t))
print(x,y)
    