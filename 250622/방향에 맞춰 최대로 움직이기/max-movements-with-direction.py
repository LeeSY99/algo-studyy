n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
direction = [list(map(int, input().split())) for _ in range(n)]
i, j = map(int, input().split())
i-=1
j-=1

di, dj = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]

ans = 0
way = []
def in_range(i,j):
    return 0<=i<n and 0<=j<n
def backtrack(count, i, j):
    global ans
    ans = max(ans, count)
    dir_index = direction[i][j]-1

    for k in range(1,n):
        ni = i+ k * di[dir_index]
        nj = j+ k * dj[dir_index]
        if in_range(ni, nj):
            if grid[ni][nj] >= grid[i][j]:
                backtrack(count+1,ni,nj)
    return

backtrack(0, i, j)
print(ans)


