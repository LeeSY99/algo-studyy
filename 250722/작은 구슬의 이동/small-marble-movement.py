n, t = map(int, input().split())


def in_range(r,c):
    return 0<r<=n and 0<c<=n

r,c,d = input().split()

drs, dcs = [0,1,0,-1],[1,0,-1,0]

direction = {'R':0, 'D':1, 'L':2, 'U':3}

r = int(r)
c = int(c)
d = direction[d]

for _ in range(t):
    nr, nc = r+drs[d], c+dcs[d]
    if not in_range(nr,nc):
        d = (d+2)%4
    else:
        r = nr
        c = nc
print(r,c)