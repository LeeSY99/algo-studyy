from collections import deque
n,m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

rr,rc = 0,0
br,bc = 0,0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'R':
            rr, rc = i,j
            grid[i][j] = '.'
        if grid[i][j] == 'B':
            br,bc = i,j
            grid[i][j] = '.'
drs, dcs = [0,1,0,-1],[1,0,-1,0]

def move(r, c, dir):
    dr, dc = drs[dir], dcs[dir]
    nr, nc = r+dr, c+dc
    dist = 0
    while True:
        if grid[nr][nc] == '#':
            return r, c, dist, False
        dist += 1
        r = nr
        c = nc
        nr = r+dr
        nc = c+dc
        if grid[r][c] == 'O':
            return r, c, dist, True

def roll(rr,rc,br,bc,dir):
    nrr,nrc,r_dist,red_inhole = move(rr,rc,dir)
    nbr,nbc,b_dist,blue_inhole = move(br,bc,dir)
    if blue_inhole:
        return

    dr, dc = drs[dir], dcs[dir]
    if not red_inhole and (nrr, nrc) == (nbr,nbc):
        if r_dist > b_dist:
            nrr -= dr
            nrc -= dc
        else:
            nbr -= dr
            nbc -= dc
    return nrr,nrc,nbr,nbc, red_inhole

def bfs(rr,rc,br,bc):
    q = deque([(rr,rc,br,bc,0)])
    visited = set([(rr, rc, br, bc)])

    while q:
        rr,rc,br,bc,depth = q.popleft()

        if depth == 10:
            continue

        for dir in range(4):
            result = roll(rr,rc,br,bc,dir)
            if not result:
                continue
            nrr,nrc,nbr,nbc,red_inhole = result
            if red_inhole:
                return depth + 1
            if (nrr,nrc,nbr,nbc) not in visited:
                q.append((nrr,nrc,nbr,nbc,depth+1))
                visited.add((nrr,nrc,nbr,nbc))

    return -1

print(bfs(rr,rc,br,bc))




