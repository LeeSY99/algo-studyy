n = int(input())

drs,dcs = [0,1,-1,0], [-1,0,0,1]
time = 0
r,c = 0,0

for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    if direction == 'W':
        d = 0
    elif direction == 'S':
        d =1
    elif direction == 'N':
        d =2
    else:
        d=3
    
    for _ in range(distance):
        time+=1
        r, c = r+drs[d], c+dcs[d]
        if r == 0 and c == 0:
            print(time)
            exit()
print(-1)
