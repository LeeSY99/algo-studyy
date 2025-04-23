n = int(input())
x, y = map(int, input().split())

grid = [['#'] * (n+2) for _ in range(n+2)]
for i in range(1,n+1):
    line = input()
    for j, ch in enumerate(line, start=1):
        grid[i][j] = ch

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def in_range(r,c):
    return 1<=r<=n and 1<=c<=n

def solve():
    r,c = x,y
    d = 0
    time = 0
    visited =set()

    while 1:
        #탈출불가능
        if (r,c,d) in visited:
            return -1
        visited.add((r,c,d))

        #다음 칸 검사 (방향전환 시계방향)
        rd = (d+1)%4
        nr, nc = r+dr[rd], c+dc[rd]

        if not in_range(nr,nc): #탈출
            return time+1
        
        if grid[nr][nc] == '.': #진행
            d=rd
            r,c=nr,nc
            time+=1
            continue
        
        #방향전환햐야 하는데 벽이면
        nr, nc = r+dr[d], c+dc[d]
        if not in_range(nr,nc):
            return time+1
        
        #진행방향 1컨 더 전진
        if grid[nr][nc] == '.':
            r,c= nr,nc
            time+=1
            continue
        #진행햐야 하는데 다음 칸이 벽이면 반시계방향 방향전환
        d=(d+3)%4
    
print(solve())