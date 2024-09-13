map = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if map[i][j]=='B':
            br=i
            bc=j
        elif map[i][j]=='R':
            rr=i
            rc=j
        elif map[i][j]=='L':
            lr=i
            lc=j

if br==rr==lr or bc==rc==lc:
    print(abs(lr-br)+abs(lc-bc)+1)
else:
    print(abs(lr-br)+abs(lc-bc)-1)