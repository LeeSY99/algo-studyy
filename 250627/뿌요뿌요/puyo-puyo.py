n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
# boom = [[0] * n for _ in range(n)]

ans = []

def in_range(i,j):
    return 0<=i<n and 0<=j<n

dis, djs = [0,1,0,-1], [1,0,-1,0]

def check(i,j,now):
    count = 0
    def dfs(i,j,now):
        nonlocal count
        if i>=n or j>=n:
            return
        count += 1
        visited[i][j] = 1

        for di, dj in zip(dis, djs):
            ni, nj = i+di, j+dj
            if in_range(ni,nj) and not visited[ni][nj] and grid[ni][nj] == now:
                dfs(ni, nj, now)

    dfs(i,j,now)
    return count

boomed = []
more_4 = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            boom = check(i,j,grid[i][j])
            boomed.append(boom)
            if boom >=4:
                more_4.append(boom)

print(len(more_4), max(boomed))

            

