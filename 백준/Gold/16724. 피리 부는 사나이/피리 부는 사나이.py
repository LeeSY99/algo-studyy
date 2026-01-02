from collections import deque
n,m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

drs = {
    'D':(1,0),
    'L':(0,-1),
    'U':(-1,0),
    'R':(0,1),
}
# print(drs[grid[1][0]])

def dfs(r,c):
    global ans
    state[r][c] = 1
    dr, dc = drs[grid[r][c]]
    nr, nc = r+dr, c+dc

    if state[nr][nc] == 0:
        dfs(nr,nc)
    elif state[nr][nc] == 1:
        ans += 1
    state[r][c] = 2

result = []
ans = 0
state = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if state[i][j] == 0:
            dfs(i,j)

print(ans)
